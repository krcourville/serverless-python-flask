# Serverless Python Flask

## Commands

```bash
# deploy the ap
sls deploy

# remove it
sls remove

# install dynamodb local (do this one time)
sls dynamodb install

# run local dev server
sls wsgi serve
```

## Why Serverless framework is awesome

- [ ] Less cloudformation to manually maintain
- [ ] Built-in support for `pipeenv`... unlike `aws sam`
- [ ] Package and deploy in one step `sls deploy`
- [ ] Documentation and community is MUCH better than that for `aws sam`
- [ ] Local development (`aws sam` has this but with limitations)
- [ ] plugins make local development a joy and not a chore
    - serverless-dynamodb-local
        * emulate dynamodb locally
        * creates tables based on serverless config (we currently do 
        this with our own script, and it's bugging/cumbersome)
    - serverless-offline:
        * emulate api gateway locally
        * emulate custom authorizers (with a caveat..)
    - serverless-plugin-warmup:
        * keep lambdas warm on a schedule
        * warm up after deployment      
    - serverless-wsgi:
        * maps AWS Api Gateway event to Flask
        * integrates with serverless-plugin-warmup to
        early exit when detecting a warm-up event
        
## What is missing?

- [ ] serverless-offline does not seem to work with python
    custom authorizer.  we're currently already
    working around this, though. as a result, `serverless-offline`
    is not useful right now

## Questions

- [ ] How to change the deployed stack name?
- [ ] "" function name?
- [ ] custom lambda authorizer?
- [ ] resource tags?

## References

* <https://serverless.com/blog/flask-python-rest-api-serverless-lambda-dynamodb/>

