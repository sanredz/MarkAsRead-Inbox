# Introduction
Personal project of mine due to the fact that my hosting provider (One.com) does not allow you to mark your entire inbox as read. I was tired of having thousands of unread emails so I wrote a short Python script to sort it out. It goes through your inbox and mark all emails as read (for services that do not include that option by default) page by page. **It won't work out of the box for any other provider than One.com.**

## Dependencies
* Python
* Selenium
* Chromedriver

## How to Use

### One.com
* Change the **driver_path** to your local path for *Chromedriver*
* Change the **webmail_url** to your email provider
* Run the script, and login to your email
* Filter your inbox for unread messages only
* Go back to your console and press *Enter*, switch back to focus on the browser window again

### Others
* Inspect your email providers UI for your specific CSS tags for:
    * **Checkbox** to mark all emails on the current page
    * **Mark as Read** button to mark them all as read
    * **Next page** button to load the next set of emails
* Replace them with the current ones in the script
* Change the **driver_path** to your local path for *Chromedriver*
* Change the **webmail_url** to your email provider
* Run the script, and login to your email
* Filter your inbox for unread messages only
* Go back to your console and press *Enter*, switch back to focus on the browser window again

## Disclaimer
This is just a personal project I made because I was tired of seeing thousands of unread emails, I did not intend for this to be any universally proven method. Use at your own risk.