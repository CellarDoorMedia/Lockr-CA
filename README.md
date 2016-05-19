# Lockr Partner Certificate Authority

Configuration and scripts for managing a Lockr compliant certificate
authority.

## Creating the Certificate Authority

```sh
$ ./script/mkca
```

You will be prompted for a key passphrase and subject information for
the CA.

## Creating Application Certificates

```sh
$ ./script/newcert.py --help
usage: newcert.py [-h] [--country COUNTRY] [--state STATE]
                  [--location LOCATION] [--org ORG] [--base-cn BASE_CN]
                  [--config CONFIG]
                  app-id env

Create new certificate.

positional arguments:
  app-id                The application ID
  env                   The application environment

optional arguments:
  -h, --help            show this help message and exit
  --country COUNTRY, -c COUNTRY
                        Certificate country
  --state STATE, -s STATE
                        Certificate state
  --location LOCATION, -l LOCATION
                        Certificate location
  --org ORG, -o ORG     Certificate organization
  --base-cn BASE_CN, -b BASE_CN
                        Certificate base common name
  --config CONFIG       Configuration file with default values (in json
                        format)
```

`country`, `state`, `location`, `org`, and `base_cn` can be specified
in the config file.

You will be prompted for the CA passphrase and confirmation of the
signing.

## Applying for Inclusion as a Lockr Partner

Send us an email at support@lockr.io with your email, name, and the
generated certificate authority.

