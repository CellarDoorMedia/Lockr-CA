#!/usr/bin/env python2
# ex: ts=4 sts=4 sw=4 et:

from argparse import ArgumentParser
import json
import os
import os.path
from os.path import dirname
import subprocess
import sys


def merge_args(args, defaults):
    names = {'country', 'state', 'location', 'org', 'base_cn'}
    merged = {}

    for name in names:
        arg = getattr(args, name)
        if arg is None:
            merged[name] = defaults[name]
        else:
            merged[name] = arg

    return merged


def create_subject(args):
    defaults = args.config

    if defaults[0] != '/':
        defaults = os.path.join(dirname(dirname(__file__)), defaults)

    with open(defaults, 'r') as f:
        defaults = json.load(f)

    arg_dict = merge_args(args, defaults)

    common = '%s.%s' % (args.env, args.app_id)
    arg_dict['common'] = common

    subject = '/' + '/'.join([
        'C=US',
        'ST={state}',
        'L={location}',
        'O={org}',
        'CN={common}.{base_cn}',
    ]).format(**arg_dict)

    ret = subprocess.call([
        'openssl', 'req', '-config', 'openssl-ca.cnf',
        '-newkey', 'rsa:2048',
        '-sha256',
        '-nodes',
        '-subj', subject,
        '-out', '%s.csr' % common,
        '-outform', 'PEM',
    ])

    if ret > 0:
        sys.exit(ret)

    os.rename('newkey.pem', '%s.key' % common)

    sign_csr(common)


def sign_csr(common):
    ret = subprocess.call([
        'openssl', 'ca', '-config', 'openssl-ca.cnf',
        '-policy', 'signing_policy',
        '-extensions', 'signing_req',
        '-out', '%s.pem' % common,
        '-infiles', '%s.csr' % common,
    ])

    if ret > 0:
        sys.exit(req)

    os.unlink('%s.csr' % common)


if __name__ == '__main__':
    parser = ArgumentParser(description='Create new certificate.')
    parser.add_argument('--country', '-c', help='Certificate country')
    parser.add_argument('--state', '-s', help='Certificate state')
    parser.add_argument('--location', '-l', help='Certificate location')
    parser.add_argument('--org', '-o', help='Certificate organization')
    parser.add_argument('--base-cn', '-b', help='Certificate base common name')
    parser.add_argument('--config', default='cert-defaults.json',
            help='Configuration file with default values (in json format)')
    parser.add_argument('app_id', metavar='app-id', help='The application ID')
    parser.add_argument('env', help='The application environment')

    args = parser.parse_args()

    create_subject(args)


