# redmine-git-fetcher
git fetcher (to cron) in redmine git directory

## requirements
- python3 or higher

## usage
- **use cron** to update continuously update your .git repository
- first, check your local directory that incldues .git folders 
> **must clone with --mirror option!!** 
> example
  ```
  /usr/share/redmine/public/git
  |- project-1.git
  |- project-2.git
  |- project-3.git
  ```
- python fetcher.py --git_dir=<directory that includes .git>
> crontab example
  ```
  */5 * * * * /usr/bin/python /cron/fetcher.py --git_dir=/usr/share/redmine/public/git
  ```

