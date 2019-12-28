# **Text Graphic Generator Webapp**

## **Development**

### **Initial Environment Setup**

1. Set up an [SSH key](https://gitlab.com/help/ssh/README#generating-a-new-ssh-key-pair) on the VM and register it with [GitLab](https://gitlab.com/) (*@eolatham*).

2. Clone the [GitLab repository](https://gitlab.com/eolatham/text-graphic-generator-webapp).

3. Run `cd text-graphic-generator-webapp` to enter the repository.

4. Run `pipenv install -r requirements.txt` to install all program dependencies in a [pipenv](https://pipenv-fork.readthedocs.io/en/latest/).

5. Run `pipenv shell` to enter the pipenv.

6. Run `cd public` to enter the public directory.

7. Run `flask run` to host the webapp on localhost.

---

## **Deployment**

### **Server Information**

- **Server type:** *[Google Cloud Platform Compute Engine VM](https://cloud.google.com/compute/)*
- **Project name:** *pioneering-mode-262914*
- **Project owner:** *ericoliverlatham*
- **VM name:** *text-graphic-generator*
- **VM zone:** *us-east1-d*
- **VM operating system:** *Ubuntu 18.04 LTS*

### **Connecting to the Server**

1. Enter [Google Cloud Shell](https://console.cloud.google.com/home/dashboard?project=pioneering-mode-262914&cloudshell=true) (or any terminal on a machine with [Google Cloud SDK](https://cloud.google.com/sdk/docs/quickstarts) installed).

2. Run `gcloud compute ssh ericoliverlatham@text-graphic-generator --project pioneering-mode-262914 --zone us-east1-d` to SSH into the VM.

### **Initial Deployment Process**

1. Run `sudo apt-get install build-essential` to install some basic packages that will be useful later.

2. Set up an [SSH key](https://gitlab.com/help/ssh/README#generating-a-new-ssh-key-pair) on the VM and register it with [GitLab](https://gitlab.com/) (*@eolatham*).

3. Clone the [GitLab repository](https://gitlab.com/eolatham/text-graphic-generator-webapp).

4. Run `cd text-graphic-generator-webapp` to enter the repository.

5. Run `make setup` to install all program dependencies.

6. Run `make deploy` to start the webapp.

### **Subsequent Deployment Process**

1. Run `cd text-graphic-generator-webapp` to enter the repository.

2. Run `git pull` to download any updated code.

3. Run `make deploy` to restart the webapp.

---

## **Future Tasks**

- Review, polish, and clarify backend code.

   - Look into reducing memory consumption.

- Look into page authentication so that only I can use it.
