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

The common name of the generated certificate will be `<env>.<app-id>.BASE_CN`.

An example of creating a certificate with a random UUID app-id:

```sh
$ ./script/newcert.py `./script/uuid` dev
Generating a 2048 bit RSA private key
...+++
.............................................+++
writing new private key to 'newkey.pem'
-----
Using configuration from openssl-ca.cnf
Enter pass phrase for ./private/cakey.pem:
Check that the request matches the signature
Signature ok
The Subject's Distinguished Name is as follows
countryName           :PRINTABLE:'US'
stateOrProvinceName   :ASN.1 12:'WA'
localityName          :ASN.1 12:'Seattle'
organizationName      :ASN.1 12:'My Partner'
commonName            :ASN.1 12:'dev.5a58857e-7224-41f3-833d-7a779be88e10.my-partner.example.com'
Certificate is to be certified until Feb 13 21:01:06 2019 GMT (1000 days)
Sign the certificate? [y/n]:y


1 out of 1 certificate requests certified, commit? [y/n]y
Write out database with 1 new entries
Data Base Updated
```

## Applying for Inclusion as a Lockr Partner

Send us an email at support@lockr.io with your email, name, and the
generated certificate authority.

