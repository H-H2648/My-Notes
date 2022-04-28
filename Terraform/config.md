For dev, service account permission can be set manually

For stage and prod, these must be done through terraform


## Go to DAP-TERRAFORM (repo)

* dev folder does nothing
* Go to modules/feature_store/buckets.tf to create buckets, service accounts permission (just follow the format)
* Create service account by modules/feature_store/service_accounts.tf
* Makes changes to both (stage and prod) by chaning the files in modules
* After making the changes:
``` 
cd stage/prod

terraform plan #compares the difference

terraform apply #to apply the change
```
* Process: make update, terraform plan (make sure it's the changwe we want), submit a pull request, once it's approved, merge it to main branch and do terraform apply (NO TERRAFORM APPLY ON OTHER BRANCHES)
* For pull request, copy/paste the terraform plan for stage/prod and put it into description