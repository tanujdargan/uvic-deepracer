## Getting Setup to train locally (optional)

Youtube Source: https://www.youtube.com/watch?v=g-bVnm-6poU
Github Source: https://github.com/aws-deepracer-community/deepracer-for-cloud?tab=readme-ov-file

Step 1: Navigate to the docs linked below.
https://aws-deepracer-community.github.io/deepracer-for-cloud/

Step 2: If you want to train using your gpu, then go ahead and install NVIDIA GPU Drivers (Game Ready or Studio Drivers depending upon your GPU)

You can skip to step 3 if you don't plan to use a GPU locally.

Step 3: Open Microsoft Store and search Ubuntu. You want to specifically install Ubuntu 22.04.5 LTS for this setup to work. Newer versions of Ubuntu require different steps that are not covered due to time constraints.

Step 4: Open the page for Ubuntu 22.04.5 LTS and install. Once that finishes, through your windows search bar or otherwise, open Ubuntu.

I do this by searching Ubuntu in the windows search bar and opening it through that.

Ubuntu will now install with WSL. This may take a few minutes depending on your hardware. Once that is done you will be prompted to setup a username and password.

Step 5: You should now be able to interact with Ubuntu.

Run: ```sudo apt update``` then run ```sudo apt upgrade``` to get all the latest packages.

Step 6: In the documentation navigate to the "Install on Windows" page.
https://aws-deepracer-community.github.io/deepracer-for-cloud/windows.html

Now run the sudo apt-get command given to install all the required packages. 

Step 7: To configure docker and/or nvidia-docker you must run each line one by one (just for safety sometimes you may run into errors)

**For now do not install CUDA Toolkit, since it makes WSL Ubuntu crash**
You should setup CUDA Toolkit now if you wish to use NVIDIA GPU look at its relevant section here: **[[For running with Nvidia GPU]]**

Step 8: Now clone the git repository into your user folder (you should already be in the user folder, you can check by running ```ls``` which should return empty)

```git clone https://github.com/aws-deepracer-community/deepracer-for-cloud.git```

Step 9: Navigate into the repository using a cd command and run
```. bin/init.sh -a cpu -c local``` replace the "cpu" with "gpu" if you're using a gpu to train.

Next run ```. bin/activate.sh run.env```. This should create the s3_minio service

Now you can run ```dr-upload-custom-files``` and ```dr-start-training``` to start training.

To view training results run ```dr-start-viewer``` and navigate to the given url

**Note: every time you open Ubuntu, run docker service by doing "sudo service docker start"**
### For running with Nvidia GPU
Go Here: https://docs.nvidia.com/cuda/wsl-user-guide/index.html

From step 3 go to this link: https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=WSL-Ubuntu&target_version=2.0&target_type=deb_local

and copy paste the install instructions into ubuntu that are shown on screen (do not change any of the on screen options)

### Currently haven't been able to get GPU Working locally.