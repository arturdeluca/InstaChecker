# IG Follower Checker

IG Follower Checker is a few programs I created to check all the followers that does not follow yours or someone's account of your choice.

## Reasoning Behind the Idea

I had the idea of this project because, back in the days, it used to have a few apps that would make it possible to check some data from your account (such as accounts that stopped following your profile). So I wanted to create something similar, since those apps are not really available anymore without getting your account banned or hacked.. 

Yeah, I can see how this might be shallow.

## Code Clarification

Before you start using it, let me explain some stuff first.

First, I am not a very good programmer at the moment (03/22/2023). I am still learning. So yes, I know the code could be more simple or cleaner. I am working on it. To just get it to work smoothly is a great achievement for me.

Secondly, I also could have followed some tutorials on the internet. It is quite easy to find them about this subject. However, I wanted to create my own project for my own needs. That is why is not too complex, but it is efficient in its own way.



## Requirement

All you need is to download the [Instaloader library](https://instaloader.github.io/).

**You need a fake/second account to use it.** Using your main account it might result in your account to be banned. Instagram does not really allow you to make too many HTTP requests that fast without access to their API. And to get their API is complicated and annoying, so that is why I use the library **Instaloader**

If trying to check on a private account, **you need to be following the target account**, otherwise it will raise a error.

## How to Use It

Alright, let's get to the fun part!

To use it is very simple.

You need to run these three programs. The order does not matter for the first two but ***not_follow_back.py*** needs to be the last one always.

1. followers.py
2. followees.py
3. not_follow_back.py

The first two files should create two different ".txt" files in the same folder as the python files. The last file will run and compare the content from those two files and determine the accounts that do not follow the account targeted back.

***Following accounts*** that are not in the ***followers.txt*** should be singled out and printed in the console.

## Troubleshooting

It should not raise any errors. However, if it does, it will probably be the **400 (Bad Request)** or the **401 (JSON query error)**

Those are **Instaloader** errors. 

To fix them, make sure your instagram account is not blocked or is pending a security verification step (such as reset password, add phone number, or something similar), or try to uninstall instaloader and install it again.

These steps should fix the issue.


## Contributing

Please, any recommendation, request, or advice is very well appreciated. 

Feel free to reach out or make adjustments.

## Disclaimer

All the code and idea of the project is to learning purposes only. The author is not trying to violate any rules of *Meta's API rules* or something similar.