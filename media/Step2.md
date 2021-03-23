# Step 2 - Configuring your Cloud infrastructure

Log into [console.cloud.google.com](https://console.cloud.google.com) using your google creds. If you do not have a google account, this is a good time to create one. Once logged in you can start your 90-day trial. They give you $300 to play around with their stuff, but we will not be using any of these tools in this project.

Go to BigQuery and start a new project.

![Image02](media/Image_002.png)

Now you have got your first project created, you can configure the access control. I have opted for the Google managed keys. Go to IAM & Admin -> Service Accounts. Add a new user askmenicely and give the user a Viewer role. Once the user has been created, click on the menu on the right and select manage keys. Create a new JSON key for this user and save it somewhere.

![Image03](media/Image_003.png)

![Image04](media/Image_004.png)

Next you need to add your admin account. Once again name your account, but this time assign it the role Owner. Do exactly the same for the admin account and save the key somewhere.
Next, we need to create a storage bucket to ingest our .orc files from. Go to storage and create a regular storage bucket. I named mine ingesting_bucket.

![Image05](media/Image_005.png)

Click on configuration. Here you will find the info required to access your bucket. You will need to enter this in Frack.

![Image06](media/Image_006.png)

That’s it. Now your cloud infra is ready for some data. Now add the data of your environment to Frack by editing the frack.py file.

![Image07](media/Image_007.png)

[Step 3 - Ingesting your first data](media/Step3.md)
