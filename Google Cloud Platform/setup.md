# Setting up Google Cloud Environment (on Mac)

Download Google Cloud SDK by following instructions here: https://cloud.google.com/sdk/docs/install

Go to terminal

```
gcloud auth login
```

This goes to the login page. Log in with the appropriate email and password

Then at the terminal enter

```
vi .bash_profile
```

This prompts to the .bash_profile file. Add the following


```
# The next line updates PATH for the Google Cloud SDK.
if [ -f '/Users/{MAC_USERNAME}/google-cloud-sdk/path.bash.inc' ]; then . '/Users/{MAC_USERNAME}/google-cloud-sdk/path.bash.inc'; fi

# The next line enables shell command completion for gcloud.
if [ -f '/Users/{MAC_USERNAME}/google-cloud-sdk/completion.bash.inc' ]; then . '/Users/{MAC_USERNAME}/google-cloud-sdk/completion.bash.inc'; fi

# Automatically enter google application credentials everytime I log in
export GOOGLE_APPLICATION_CREDENTIALS=/Users/{MAC_USERNAME}/.config/gcloud/legacy_credentials/{GCP_ACCOUNT}/adc.json
```

Note that the directory must change appropriately (hunter.h refers to the home directory)

This ensures that we have an automatic authentication (that our account would have) whenever running gcp on sdk's.