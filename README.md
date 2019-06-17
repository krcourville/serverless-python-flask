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

## Serverless Framework Analysis

### The Bullet Points

- [ ] Less cloudformation to manually maintain
- [ ] Outputs to cloudformation, so SLS can easily be discarded as a result or
we can use Serverless as a starting point if we want.
- [ ] Built-in support for `pipeenv`... unlike `aws sam`
- [ ] Package and deploy in one step `sls deploy`
- [ ] Documentation and community is MUCH better than that for `aws sam`
 (though, in some areas, Python)
- [ ] Local development (`aws sam` has this but with limitations)
- [ ] plugins help to improve workflow and solve common problems
    - serverless-dynamodb-local
        * emulate dynamodb locally
        * creates tables based on serverless config (we currently do 
        this with our own script, and it's buggy/cumbersome)
    - serverless-offline:
        * emulate api gateway locally
        * emulate custom authorizers (only supports Nodejs runtime)
    - serverless-offline-python
        * same as above
        * only supports Python 3.6
    - serverless-plugin-warmup:
        * keep lambdas warm on a schedule
        * warm up on deployment (requires using `sls deploy`)    
        * effectively solves the warm-up problem, assuming we
        monitor and ensure we have enough instances warmed up
    - serverless-wsgi:
        * maps AWS Api Gateway event to Flask
        * integrates with serverless-plugin-warmup to
        early exit when detecting a warm-up event
        
## References

* <https://serverless.com/blog/flask-python-rest-api-serverless-lambda-dynamodb/>

