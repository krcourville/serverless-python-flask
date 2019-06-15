# Serverless Python Flask

## Commands

```bash
# deploy the ap
sls deploy

# remove it
sls remove

# install dynamodb local (do this one time)
sls dynamodb install

# start dynamodb
sls dynamodb start

# run local dev server
sls wsgi serve
```

## Why Serverless framework is awesome

- [ ] Less cloudformation to manually maintain
- [ ] Built-in support for `pipeenv`... unlike `aws sam`
- [ ] Package and deploy in one step `sls deploy`
- [ ] Documentation is MUCH better than that for `aws sam`
- [ ] Local development (`aws sam` has this... but)
- [ ] plugins make local development a joy and not a chore
    -  serverless-dynamodb-local

## Questions

- [ ] How to change the deployed stack name?
- [ ] "" function name?
- [ ] running locally?
- [ ] custom lambda 
- [ ] VPC's!
- [ ] resource tags?

## References

* <https://serverless.com/blog/flask-python-rest-api-serverless-lambda-dynamodb/>

