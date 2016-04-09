# webhooker

> Your own deployment whore

**DISCLAIMER:** This is my first Python script, so I appreciate code review and feedback of any kind.

-----

A Python script to listen for pings from Bitbucket. Runs `fab deploy` in specified folder.


## Configuration and usage

Set up a webhook with URL like this: `/<project>?branch=<branchname>`. `project` will resolve to `/var/www/<project>` folder which is used as CWD. `branchname` is the name of branch which will trigger deployment.

On your server run this script `python webhooker.py`. You can add a port number if `8080` doesn’t look like your port of choice: `python webhooker.py 12345`.


## Future

This is a quick and dirty project. I started it to put my hands on Python. But this doesn’t mean I have no plans. It would be nice to support HTTPS and to configure everything with hook URL and query string. I’m open for suggestions; don’t hesitate.


## License

MIT © [Leonard Kinday](mailto:leonard@kinday.ru)
