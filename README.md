# Spotify Data Scraper

The goal of this project is to create an open source method for keeping track of your spotify data. Right now this program just pulls data and stores it in a firestore instance, but I want to make it so the user can swap out storage methods with their preferred method of storage. I also want to add analytics and tracking methods to this project.

# Instructions for Running

Run the build command to install necessary dependencies
```bash
source build.sh
```

## Setting up Necessary Environment

1. Set up a Spotify Developer account and create a project on the [Spotify Developer Portal](https://developer.spotify.com/)

2. Set up a GCP account and a project using the [GCP Console](https://console.cloud.google.com/welcome)

3. Create a service account and private key for your project on the [IAM and Admin Page](https://console.cloud.google.com/iam-admin/serviceaccounts)

4. When creating a Private Key, select the JSON option. The downloaded .json should contain all of the information necessary for filling out the .env file.

5. Create a .env file with the following entries:
```bash
# Spotify
CLIENT_ID=<SPOTIFY PROJECT CLIENT ID>
CLIENT_SECRET=<SPOTIFY PROJECT CLIENT SECRET>
REDIRECT_URI=<SPOTIFY PROJECT REDIRECT URI>

# Google Cloud
CLIENT_EMAIL=<GCP PROJECT SERVICE EMAIL>
PROJECT_ID=<GCP PROJECT ID>
PRIVATE_KEY=<GOOGLE CLOUD PRIVATE KEY FOR CORRESPONDING GCP PROJECT>
```

## Running as a Background Process

Run the following command and don't stop it
```bash
python worker.py
```

## Running as a Cron Job

If you want to run this program as a cron job, set the command to run as
```bash
python cron.py
```

Feel free to choose the frequency at which you want the program. I've found that running it every 125 minutes is a pretty safe amount. 
```bash
*/125 * * * *
```
For people who listen to shorter songs, having it run every hour should be more than enough
```bash
0 * * * *
```
