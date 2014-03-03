there-will-be-blood
===================

Our app for Freshdesk hackathon. 

At the application end:

You install the app and register with phone number and location. Once the app is installed you will get notifications that match your location.

At the server:

- Pulls tweets mentioning a pre-coded set of keywords which we think would fetch tweets asking for blood donations. Extracts three key parameters from each tweet: Location (does not use location provided by Twitter), contact number and blood group.

- We use Google's cloud messaging service to send push notifications to people who match the location asked for in the tweet. 


Features:

- Matches users using location. We debated on whether or not to filter using blood group and finally decided against it.

- Users have a Do not disturb option that takes parameters in terms of days and it can be toggled on or off.

- Users can change their locations manually as and when they move to different cities across the globe.

- People asking for blood donations need not change their tweet format and can tweet anything as long as the tweet contains blood group, location and phone number.

- To avoid duplicate notifications resulting from re-tweets we check the phone number from the tweet and send notification only if the same phone number had not asked for donations previously any given day.

- If you had taken antibiotics or have consumed alcohol, you can toggle the "Have you partied recently?" question on the app. If you choose yes, we will not send you notifications for the next 2 days.

To do:

- Adding a facility for donors to place request through the app. This will result in us tweeting the request, which in turn will result in notifications being sent to all our users.

- Extend posting abilities to Facebook. 

- Extend searching abilities to Facebook.

- Scale up and handle concurrent requests (mostly PubSub)


