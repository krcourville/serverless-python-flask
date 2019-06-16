def handle(event, context):
    authorization_token = event.get('authorizationToken', None)

    def deny_access():
        return generate_policy('user_a', 'DENY', '*')

    if not authorization_token:
        return deny_access()

    token_type, token_value = authorization_token.split(' ')
    if token_type.lower() != 'bearer' or token_value != '1234':
        return deny_access()

    policy = generate_policy('user_a', 'ALLOW', event.get('methodArn'))

    return policy


def generate_policy(principal_id, effect, resource):
    auth_response = {'principalId': principal_id}
    if effect and resource:
        policy_document = dict(
            Version='2012-10-17',
            Statement=[
                dict(
                    Action='execute-api:Invoke',
                    Effect=effect,
                    resource=resource
                )
            ]

        )
        auth_response['policyDocument'] = policy_document

    return auth_response
