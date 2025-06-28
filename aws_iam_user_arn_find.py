import boto3

def list_iam_user_arns():
    iam = boto3.client('iam')

    paginator = iam.get_paginator('list_users')
    page_iterator = paginator.paginate()
    b=[]
    print("IAM User ARNs:")
    for page in page_iterator:
        for user in page['Users']:
            b.append(user['Arn'])
    return(b)
if __name__ == "__main__":
    arn_list=list_iam_user_arns()
    for arn in arn_list:
        print(arn.split("/")[1].upper())

