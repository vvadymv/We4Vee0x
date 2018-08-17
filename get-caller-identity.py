#!/usr/bin/env python
import boto3

# playtech.com

access_key = 'AKIAICDFTTNOXYO2FJFA'
secret_key = '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'

def get_aws_account_id(access_key, secret_key):
    sts = boto3.client(
        "sts", aws_access_key_id=access_key, aws_secret_access_key=secret_key,
    )
    user_arn = sts.get_caller_identity()["Arn"]

    return user_arn.split(":")[4]

print get_aws_account_id(access_key, secret_key)
