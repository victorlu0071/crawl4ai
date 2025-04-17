# Content from: https://www.pythonguis.com/tutorials/git-github-python/

[](https://www.pythonguis.com/tutorials/git-github-python/#menu)
  * Python GUIs
  * [Home](https://www.pythonguis.com/)
  * [Latest Articles](https://www.pythonguis.com/latest/)
  * [FAQ](https://www.pythonguis.com/faq/)
  * [Forum ](https://forum.pythonguis.com/)
  * Resources
  * [Books](https://www.pythonguis.com/books/)
  * Services
  * [Consulting](https://www.pythonguis.com/hire/)
  * [1:1 Coaching](https://www.pythonguis.com/live/)
  * [Contact](https://www.pythonguis.com/contact/)
  * [About](https://www.pythonguis.com/about/)
  * Libraries
  * [PyQt6](https://www.pythonguis.com/pyqt6/)
  * [PySide6](https://www.pythonguis.com/pyside6/)
  * [PyQt5](https://www.pythonguis.com/pyqt5/)
  * [Streamlit](https://www.pythonguis.com/streamlit/)
  * [Tkinter](https://www.pythonguis.com/tkinter/)
  * [PySide2](https://www.pythonguis.com/pyside2/)


  * Search Python GUIs


[](https://www.pythonguis.com "Python GUIs")
Search Python GUIs
# Getting Started With Git and GitHub in Your Python Projects
Version-Controlling Your Python Projects With Git and GitHub
by [Lalin Paranawithana](https://www.pythonguis.com/authors/lalin-paranawithana/) Last updated Apr 08 [ Tutorials ](https://www.pythonguis.com/tutorials/)
Using a [version control system (VCS)](https://en.wikipedia.org/wiki/Version_control) is crucial for any software development project. These systems allow developers to track changes to the project's codebase over time, removing the need to keep multiple copies of the project folder.
VCSs also facilitate experimenting with new features and ideas without breaking existing functionality in a given project. They also enable collaboration with other developers that can contribute code, documentation, and more.
In this article, we'll learn about [Git](https://git-scm.com/), the most popular VCS out there. We'll learn everything we need to get started with this VCS and start creating our own repositories. We'll also learn how to publish those repositories to [GitHub](https://github.com/about), another popular tool among developers nowadays.
Table of Contents
  * [Installing and Setting Up Git](https://www.pythonguis.com/tutorials/git-github-python/#installing-and-setting-up-git)
  * [Understanding How Git Works](https://www.pythonguis.com/tutorials/git-github-python/#understanding-how-git-works)
  * [Version-Controlling a Project With Git: The Basics](https://www.pythonguis.com/tutorials/git-github-python/#version-controlling-a-project-with-git-the-basics)
    * [Initializing a Git Repository](https://www.pythonguis.com/tutorials/git-github-python/#initializing-a-git-repository)
    * [Checking the Status of Our Project](https://www.pythonguis.com/tutorials/git-github-python/#checking-the-status-of-our-project)
    * [Tracking and Committing Changes](https://www.pythonguis.com/tutorials/git-github-python/#tracking-and-committing-changes)
    * [Using a .gitignore File to Skip Unneeded Files](https://www.pythonguis.com/tutorials/git-github-python/#using-a-gitignore-file-to-skip-unneeded-files)
  * [Working With Branches in Git](https://www.pythonguis.com/tutorials/git-github-python/#working-with-branches-in-git)
    * [Creating New Branches](https://www.pythonguis.com/tutorials/git-github-python/#creating-new-branches)
    * [Checking Out to a New Branch](https://www.pythonguis.com/tutorials/git-github-python/#checking-out-to-a-new-branch)
    * [Merging Two Branches Together](https://www.pythonguis.com/tutorials/git-github-python/#merging-two-branches-together)
    * [Deleting Unused Branches](https://www.pythonguis.com/tutorials/git-github-python/#deleting-unused-branches)
  * [Using a GUI Client for Git](https://www.pythonguis.com/tutorials/git-github-python/#using-a-gui-client-for-git)
  * [Managing a Project With GitHub](https://www.pythonguis.com/tutorials/git-github-python/#managing-a-project-with-github)
    * [Setting Up a Secure Connection to GitHub](https://www.pythonguis.com/tutorials/git-github-python/#setting-up-a-secure-connection-to-github)
    * [Creating and Setting Up a GitHub Repository](https://www.pythonguis.com/tutorials/git-github-python/#creating-and-setting-up-a-github-repository)
    * [Pushing a Local Git Repository to GitHub](https://www.pythonguis.com/tutorials/git-github-python/#pushing-a-local-git-repository-to-github)
    * [Pulling Content From a GitHub Repository](https://www.pythonguis.com/tutorials/git-github-python/#pulling-content-from-a-github-repository)
    * [Exploring Alternatives to GitHub](https://www.pythonguis.com/tutorials/git-github-python/#exploring-alternatives-to-github)
  * [Conclusion](https://www.pythonguis.com/tutorials/git-github-python/#conclusion)


## Installing and Setting Up Git
To use Git in our coding projects, we first need to install it on our computer. To do this, we need to navigate to Git's [download page](https://git-scm.com/downloads) and choose the appropriate installer for our operating system. Once we've downloaded the installer, we need to run it and follow the on-screen instructions.
We can check if everything is working correctly by opening a terminal or command-line window and running `git --version`.
Once we've confirmed the successful installation, we should provide Git with some personal information. You'll only need to do this once for every computer. Now go ahead and run the following commands with your own information:
shell ```
$ git config --global user.name <"YOUR NAME">
$ git config --global user.email <name@email.com>

```

The first command adds your full name to Git's config file. The second command adds your email. Git will use this information in all your repositories.
1:1 Coaching & Tutoring for your Python GUIs project
[![Martin Fitzpatrick Python GUIs Coaching & Training](https://www.pythonguis.com/static/theme/images/products/coaching.jpg)](https://calendly.com/martinfitzpatrick/60min-python-guis-coaching)
[60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/) [Book Now](https://www.pythonguis.com/live/)
1:1 Python GUIs Coaching & Training
**Comprehensive code review** • **Bugfixes** & improvements • **Maintainability** advice and **architecture** improvements • **Design and usability** assessment • Suggestions and tips to **expand your knowledge** • **Packaging and distribution** help for Windows, Mac & Linux • [Find out more.](https://www.pythonguis.com/live)
If you publish your projects to a remote server like GitHub, then your email address will be visible to anyone with access to that repository. If you don't want to expose your email address this way, then you should create a separate email address to use with Git.
As you'll learn in a moment, Git uses the concept of **branches** to manage its repositories. A branch is a copy of your project's folder at a given time in the development cycle. The default branch of new repositories is named either `master` or `main`, depending on your current version of Git.
You can change the name of the default branch by running the following command:
shell ```
$ git config --global init.defaultBranch <branch_name>

```

This command will set the name of Git's default branch to `branch_name`. Remember that this is just a placeholder name. You need to provide a suitable name for your installation.
Another useful setting is the default text editor Git will use to type in commit messages and other messages in your repo. For example, if you use an editor like Visual Studio Code, then you can configure Git to use it:
shell ```
# Visual Studio Code
$ git config --global core.editor "code --wait"

```

With this command, we tell Git to use VS Code to process commit messages and any other message we need to enter through Git.
Finally, to inspect the changes we've made to Git's configuration files, we can run the following command:
shell ```
$ git config --global -e

```

This command will open the global `.gitconfig` file in our default editor. There, we can fix any error we have made or add new settings. Then we just need to save the file and close it.
## Understanding How Git Works
Git works by allowing us to take a _snapshot_ of the current state of all the files in our project's folder. Each time we save one of those snapshots, we make a Git **commit**. Then the cycle starts again, and Git creates new snapshots, showing how our project looked like at any moment.
Git was created in 2005 by [Linus Torvalds](https://en.wikipedia.org/wiki/Linus_Torvalds), the creator of the [Linux kernel](https://en.wikipedia.org/wiki/Linux_kernel). Git is an [open-source](https://www.pythonguis.com/faq/charge-for-open-source-software/) project that is licensed under the [GNU General Public License (GPL) v2](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html). It was initially made to facilitate kernel development due to the lack of a suitable alternative.
The general workflow for making a Git commit to saving different snapshots goes through the following steps:
  1. **Change** the content of our project's folder.
  2. **Stage** or mark the changes we want to save in our next commit.
  3. **Commit** or save the changes permanently in our project's Git database.


As the third step mentions, Git uses a special database called a **repository**. This database is kept inside your project's directory under a folder called `.git`.
## Version-Controlling a Project With Git: The Basics
In this section, we'll create a local repository and learn how to manage it using the Git [command-line interface (CLI)](https://en.wikipedia.org/wiki/Command-line_interface). On macOS and Linux, we can use the default terminal application to follow along with this tutorial.
On Windows, we recommend using Git Bash, which is part of the [Git For Windows](https://gitforwindows.org/) package. Go to the Git Bash download page, get the installer, run it, and follow the on-screen instruction. Make sure to check the _Additional Icons_ -> _On the Desktop_ to get direct access to Git Bash on your desktop so that you can quickly find and launch the app.
Alternatively, you can also use either Windows' Command Prompt or [PowerShell](https://learn.microsoft.com/en-us/powershell/). However, some commands may differ from the commands used in this tutorial.
### Initializing a Git Repository
To start version-controlling a project, we need to initialize a new Git repository in the project's root folder or directory. In this tutorial, we'll use a sample project to facilitate the explanation. Go ahead and create a new folder in your file system. Then navigate to that folder in your terminal by running these commands:
shell ```
$ mkdir sample_project
$ cd sample_project

```

The first command creates the project's root folder or directory, while the second command allows you to navigate into that folder. Don't close your terminal window. You'll be using it throughout the next sections.
To initialize a Git repository in this folder, we need to use the [`git init`](https://git-scm.com/docs/git-init) command like in the example below:
shell ```
$ git init
Initialized empty Git repository in /.../sample_project/.git/

```

This command creates a subfolder called `.git` inside the project's folder. The leading dot in the folder's name means that this is a hidden directory. So, you may not see anything on your file manager. You can check the existence of `.git` with the `ls -a`, which lists all files in a given folder, including the hidden ones.
### Checking the Status of Our Project
Git provides the [`git status`](https://git-scm.com/docs/git-status) command to allow us to identify the current state of a Git repository. Because our `sample_project` folder is still empty, running `git status` will display something like this:
shell ```
$ git status
On branch main
No commits yet
nothing to commit (create/copy files and use "git add" to track)

```

When we run `git status`, we get detailed information about the current state of our Git repository. This command is pretty useful, and we'll turn back to it in multiple moments.
As an example of how useful the `git status` command is, go ahead and create a file called `main.py` inside the project's folder using the following commands:
shell ```
$ touch main.py

$ git status
On branch main
No commits yet
Untracked files:
 (use "git add <file>..." to include in what will be committed)
  main.py
nothing added to commit but untracked files present (use "git add" to track)

```

With the [`touch`](https://en.wikipedia.org/wiki/Touch_\(command\)) command, we create a new `main.py` file under our project's folder. Then we run `git status` again. This time, we get information about the presence of an untracked file called `main.py`. We also get some basic instructions on how to add this file to our Git repo. Providing these guidelines or instructions is one of the neatest features of `git status`.
Now, what is all that about untracked files? In the following section, we'll learn more about this topic.
### Tracking and Committing Changes
A file in a Git repository can be either **tracked** or **untracked**. Any file that wasn't present in the last commit is considered an untracked file. Git doesn't keep a history of changes for untracked files in your project's folder.
In our example, we haven't made any commits to our Git repo, so `main.py` is naturally untracked. To start tracking it, run the [`git add`](https://git-scm.com/docs/git-add) command as follows:
shell ```
$ git add main.py

$ git status
On branch main
No commits yet
Changes to be committed:
 (use "git rm --cached <file>..." to unstage)
  new file:  main.py

```

This `git add` command has added `main.py` to the list of tracked files. Now it's time to save the file permanently using the [`git commit`](https://git-scm.com/docs/git-commit) command with an appropriate commit message provided with the `-m` option:
shell ```
$ git commit -m "Add main.py"
[main (root-commit) 5ac6586] Add main.py
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 main.py

$ git status
On branch master
nothing to commit, working tree clean

```

We have successfully made our first commit, saving `main.py` to our Git repository. The `git commit` command requires a commit message, which we can provide through the `-m` option. Commit messages should clearly describe what we have changed in our project.
After the commit, our `main` branch is completely clean, as you can conclude from the `git status` output.
Now let's start the cycle again by modifying `main.py`, staging the changes, and creating a new commit. Go ahead and run the following commands:
shell ```
$ echo "print('Hello, World!')" > main.py
$ cat main.py
print('Hello, World!')

$ git add main.py

$ git commit -m "Create a 'Hello, World!' script on main.py"
[main 2f33f7e] Create a 'Hello, World!' script on main.py
 1 file changed, 1 insertion(+)

```

The [`echo`](https://en.wikipedia.org/wiki/Echo_\(command\)) command adds the statement `"print('Hello, World!')"` to our `main.py` file. You can confirm this addition with the [`cat`](https://en.wikipedia.org/wiki/Cat_\(Unix\)) command, which lists the content of one or more target files. You can also open `main.py` in your favorite editor and update the file there if you prefer.
We can also use the [`git stage`](https://git-scm.com/docs/git-stage) command to stage or add files to a Git repository and include them in our next commit.
We've made two commits to our Git repo. We can list our **commit history** using the [`git log`](https://git-scm.com/docs/git-log) command as follows:
shell ```
$ git log --oneline
2f33f7e (HEAD -> main) Create a 'Hello, World!' script on main.py
5ac6586 Add main.py

```

The `git log` command allows us to list all our previous commits. In this example, we've used the `--oneline` option to list commits in a single line each. This command takes us to a dedicated output space. To leave that space, we can press the letter `Q` on our keyboard.
### Using a `.gitignore` File to Skip Unneeded Files
While working with Git, we will often have files and folders that we must not save to our Git repo. For example, most Python projects include a `venv/` folder with a virtual environment for that project. Go ahead and create one with the following command:
shell ```
$ python -m venv venv

```

Once we've added a Python virtual environment to our project's folder, we can run `git status` again to check the repo state:
shell ```
$ git status
On branch main
Untracked files:
 (use "git add <file>..." to include in what will be committed)
  venv/
nothing added to commit but untracked files present (use "git add" to track)

```

Now the `venv/` folder appears as an untracked file in our Git repository. We don't need to keep track of this folder because it's not part of our project's codebase. It's only a tool for working on the project. So, we need to ignore this folder. To do that, we can add the folder to a `.gitignore` file.
Go ahead and create a `.gitignore` file in the project's folder. Add the `venv/` folders to it and run `git status`:
shell ```
$ touch .gitignore
$ echo "venv/" > .gitignore
$ git status
On branch main
Untracked files:
 (use "git add <file>..." to include in what will be committed)
  .gitignore
nothing added to commit but untracked files present (use "git add" to track)

```

Now `git status` doesn't list `venv/` as an untracked file. This means that Git is ignoring that folder. If we take a look at the output, then we'll see that `.gitignore` is now listed as an untracked file. We must commit our `.gitignore` files to the Git repository. This will prevent other developers working with us from having to create their own local `.gitignore` files.
We can also list multiple files and folders in our `.gitignore` file one per line. The file even accepts [glob patterns](https://en.wikipedia.org/wiki/Glob_\(programming\)) to match specific types of files, such as `*.txt`. If you want to save yourself some work, then you can take advantage of GitHub's [gitignore](https://github.com/github/gitignore) repository, which provides a rich list of predefined `.gitignore` files for different programming languages and development environments.
We can also set up a global `.gitignore` file on our computer. This global file will apply to all our Git repositories. If you decide to use this option, then go ahead and create a `.gitignore_global` in your home folder.
## Working With Branches in Git
One of the most powerful features of Git is that it allows us to create multiple branches. A **branch** is a copy of our project's current status and commits history. Having the option to create and handle branches allows us to make changes to our project without messing up the main line of development.
We'll often find that software projects maintain several independent branches to facilitate the development process. A common branch model distinguishes between four different types of branches:
  1. A `main` or `master` branch that holds the main line of development
  2. A `develop` branch that holds the last developments
  3. One or more `feature` branches that hold changes intended to add new features
  4. One or more `bugfix` branches that hold changes intended to fix critical bugs


However, the branching model to use is up to you. In the following sections, we'll learn how to manage branches using Git.
### Creating New Branches
Working all the time on the `main` or `master` branch isn't a good idea. We can end up creating a mess and breaking the code. So, whenever we want to experiment with a new idea, implement a new feature, fix a bug, or just refactor a piece of code, we should create a new branch.
To kick things off, let's create a new branch called `hello` on our Git repo under the `sample_project` folder. To do that, we can use the [`git branch`](https://git-scm.com/docs/git-branch) command followed by the branch's name:
shell ```
$ git branch hello
$ git branch --list
* main
 hello

```

The first command creates a new branch in our Git repo. The second command allows us to list all the branches that currently exist in our repository. Again, we can press the letter `Q` on our keyboard to get back to the terminal prompt.
The star symbol denotes the currently active branch, which is `main` in the example. We want to work on `hello`, so we need to activate that branch. In Git's terminology, we need to check out to `hello`.
### Checking Out to a New Branch
Although we have just created a new branch, in order to start working on it, we need to _switch_ to or check out to it by using the [`git checkout`](https://git-scm.com/docs/git-checkout) command as follows:
shell ```
$ git checkout hello
Switched to branch 'hello'

$ git branch --list
 main
* hello

$ git log --oneline
2f33f7e (HEAD -> hello, main) Create a 'Hello, World!' script on main.py
5ac6586 Add main.py

```

The `git checkout` command takes the name of an existing branch as an argument. Once we run the command, Git takes us to the target branch.
We can derive a new branch from whatever branch we need.
As you can see, `git branch --list` indicates which branch we are currently on by placing a `*` symbol in front of the relevant branch name. If we check the commit history with `git log --oneline`, then we'll get the same as we get from `main` because `hello` is a copy of it.
The `git checkout` can take a `-b` flag that we can use to create a new branch and immediately check out to it in a single step. That's what most developers use while working with Git repositories. In our example, we could have run `git checkout -b hello` to create the `hello` branch and check out to it with one command. 
#### Never miss an update
Enjoyed this? Subscribe to get new updates straight in your Inbox.
Subscribe 
You can unsubscribe anytime. Just ham, no spam.
Let's make some changes to our project and create another commit. Go ahead and run the following commands:
shell ```
$ echo "print('Welcome to PythonGUIs!')" >> main.py
$ cat main.py
print('Hello, World!')
print('Welcome to PythonGUIs!')

$ git add main.py
$ git commit -m "Extend our 'Hello, World' program with a welcome message."
[hello be62476] Extend our 'Hello, World' program with a welcome message.
 1 file changed, 1 insertion(+)

```

The final command committed our changes to the `hello` branch. If we compare the commit history of both branches, then we'll see the difference:
shell ```
$ git log --oneline -1
be62476 (HEAD -> hello) Extend our 'Hello, World' program with a welcome message.

$ git checkout main
Switched to branch 'main'

$ git log --oneline -1
2f33f7e (HEAD -> main) Create a 'Hello, World!' script on main.py

```

In this example, we first run `git log --oneline` with `-1` as an argument. This argument tells Git to give us only the last commit in the active branch's commit history. To inspect the commit history of `main`, we first need to check out to that branch. Then we can run the same `git log` command.
Now say that we're happy with the changes we've made to our project in the `hello` branch, and we want to update `main` with those changes. How can we do this? We need to merge `hello` into `main`.
### Merging Two Branches Together
To add the commits we've made in a separate branch back to another branch, we can run what is known as a **merge**. For example, say we want to merge the new commits in `hello` into `main`. In this case, we first need to switch back to `main` and then run the [`git merge`](https://git-scm.com/docs/git-merge) command using `hello` as an argument:
shell ```
$ git checkout main
Already on 'main'

$ git merge hello
Updating 2f33f7e..be62476
Fast-forward
 main.py | 1 +
 1 file changed, 1 insertion(+)

```

To merge a branch into another branch, we first need to check out the branch we want to update. Then we can run `git merge`. In the example above, we first check out to `main`. Once there, we can merge `hello`.
### Deleting Unused Branches
Once we've finished working in a given branch, we can delete the entire branch to keep our repo as clean as possible. Following our example, now that we've merged `hello` into `main`, we can remove `hello`.
To remove a branch from a Git repo, we use the `git branch` command with the `--delete` option. To successfully run this command, make sure to switch to another branch before:
shell ```
$ git checkout main
Already on 'main'

$ git branch --delete hello
Deleted branch hello (was be62476).

$ git branch --list
* main

```

Deleting unused branches is a good way to keep our Git repositories clean, organized, and up to date. Also, deleting them as soon as we finish the work is even better because having old branches around may be confusing for other developers collaborating with our project. They might end up wondering why these branches are still alive.
## Using a GUI Client for Git
In the previous sections, we've learned to use the `git` command-line tool to manage Git repositories. If you prefer to use GUI tools, then you'll find a bunch of third-party GUI frontends for Git. While they won't completely replace the need for using the command-line tool, they can simplify your day-to-day workflow.
You can get a complete list of standalone GUI clients available on the Git [official documentation](https://git-scm.com/downloads/guis).
Most popular IDEs and code editors, including [PyCharm](https://www.jetbrains.com/pycharm/) and [Visual Studio Code](https://www.pythonguis.com/tutorials/getting-started-vs-code-python/), come with basic Git integration out-of-the-box. Some developers will prefer this approach as it is directly integrated with their development environment of choice.
If you need something more advanced, then [GitKraken](https://www.gitkraken.com) is probably a good choice. This tool provides a standalone, cross-platform GUI client for Git that comes with many additional features that can boost your productivity.
## Managing a Project With GitHub
If we publish a project on a remote server with support for Git repositories, then anyone with appropriate permissions can [clone](https://git-scm.com/docs/git-clone) our project, creating a local copy on their computer. Then, they can make changes to our project, commit them to their local copy, and finally push the changes back to the remote server. This workflow provides a straightforward way to allow other developers to contribute code to your projects.
In the following sections, we'll learn how to create a remote repository on GitHub and then push our existing local repository to it. Before we do that, though, head over to [GitHub.com](https://github.com/) and create an account there if you don't have one yet. Once you have a GitHub account, you can set up the connection to that account so that you can use it with Git.
### Setting Up a Secure Connection to GitHub
In order to work with GitHub via the `git` command, we need to be able to authenticate ourselves. There are a few ways of doing that. However, using [SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/about-ssh) is the recommended way. The first step in the process is to generate an SSH key, which you can do with the following command:
shell ```
$ ssh-keygen -t ed25519 -C "GitHub - name@email.com"

```

Replace the placeholder email address with the address you've associated with your GitHub account. Once you run this command, you'll get three different prompts in a row. You can respond to them by pressing Enter to accept the default option. Alternatively, you can provide custom responses.
Next, we need to copy the contents of our `id_ed25519.pub` file. To do this, you can run the following command:
shell ```
$ cat ~/.ssh/id_ed25519.pub

```

Select the command's output and copy it. Then go to your GitHub _Settings_ page and click the _SSH and GPG keys_ option. There, select _New SSH key_ , set a descriptive title for the key, make sure that the _Key Type_ is set to _Authentication Key_ , and finally, paste the contents of `id_ed25519.pub` in the _Key_ field. Finally, click the _Add SSH key_ button.
At this point, you may be asked to provide some kind of [Two-Factor Authentication (2FA)](https://en.wikipedia.org/wiki/Multi-factor_authentication) code. So, be ready for that extra security step.
Now we can test our connection by running the following command:
shell ```
$ ssh -T git@github.com
The authenticity of host 'github.com (IP ADDRESS)' can not be established.
ECDSA key fingerprint is SHA256:p2QAMXNIC1TJYWeIOttrVc98/R1BUFWu3/LiyKgUfQM.
Are you sure you want to continue connecting (yes/no/[fingerprint])?

```

Make sure to check whether the key fingerprint shown on your output matches [GitHub's public key fingerprint](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/githubs-ssh-key-fingerprints). If it matches, then enter _yes_ and press Enter to connect. Otherwise, don't connect.
If the connection is successful, we will get a message like this:
shell ```
Hi USERNAME! You have successfully authenticated, but GitHub does not provide shell access.

```

Congrats! You've successfully connected to GitHub via SSH using a secure SSH key. Now it's time to start working with GitHub.
### Creating and Setting Up a GitHub Repository
Now that you have a GitHub account with a proper SSH connection, let's create a remote repository on GitHub using its web interface. Head over to the GitHub page and click the `+` icon next to your avatar in the top-right corner. Then select _New repository_.
Give your new repo a unique name and choose who can see this repository. To continue with our example, we can give this repository the same name as our local project, `sample_project`.
To avoid conflicts with your existing local repository, don't add `.gitignore`, `README`, or `LICENSE` files to your remote repository.
Next, set the repo's visibility to _Private_ so that no one else can access the code. Finally, click the _Create repository_ button at the end of the page.
If you create a _Public_ repository, make sure also to choose an [open-source license](https://choosealicense.com) for your project to tell people what they can and can't do with your code.
You'll get a _Quick setup_ page as your remote repository has no content yet. Right at the top, you'll have the choice to connect this repository via HTTPS or SSH. Copy the SSH link and run the following command to tell Git where the remote repository is hosted:
shell ```
$ git remote add origin git@github.com:USERNAME/sample_project.git

```

This command adds a new remote repository called `origin` to our local Git repo.
The name `origin` is commonly used to denote the main remote repository associated with a given project. This is the default name Git uses to identify the main remote repo.
Git allows us to add several remote repositories to a single local one using the `git remote add` command. This allows us to have several remote copies of your local Git repo.
### Pushing a Local Git Repository to GitHub
With a new and empty GitHub repository in place, we can go ahead and push the content of our local repo to its remote copy. To do this, we use the `git push` command providing the target remote repo and the local branch as arguments:
shell ```
$ git push -u origin main
Enumerating objects: 9, done.
Counting objects: 100% (9/9), done.
Delta compression using up to 8 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (9/9), 790 bytes | 790.00 KiB/s, done.
Total 9 (delta 0), reused 0 (delta 0), pack-reused 0
To github.com:USERNAME/sample_project.git
 * [new branch]   main -> main
branch 'main' set up to track 'origin/main'.

```

This is the first time we push something to the remote repo `sample_project`, so we use the `-u` option to tell Git that we want to set the local `main` branch to track the remote `main` branch. The command's output provides a pretty detailed summary of the process.
Note that if you don't add the `-u` option, then Git will ask what you want to do. A safe workaround is to copy and paste the commands GitHub suggests, so that you don't forget `-u`.
Using the same command, we can push any local branch to any remote copy of our project's repo. Just change the repo and branch name: `git push -u remote_name branch_name`.
Now let's head over to our browser and refresh the GitHub page. We will see all of our project files and commit history there.
Now we can continue developing our project and making new commits locally. To push our commits to the remote `main` branch, we just need to run `git push`. This time, we don't have to use the remote or branch name because we've already set `main` to track `origin/main`.
### Pulling Content From a GitHub Repository
We can do basic file editing and make commits within GitHub itself. For example, if we click the `main.py` file and then click the _pencil_ icon at the top of the file, we can add another line of code and commit those changes to the remote `main` branch directly on GitHub.
Go ahead and add the statement `print("Your Git Tutorial is Here...")` to the end of `main.py`. Then go to the end of the page and click the _Commit changes_ button. This makes a new commit on your remote repository.
This remote commit won't appear in your local commit history. To download it and update your local `main` branch, use the [`git pull`](https://git-scm.com/docs/git-pull) command:
shell ```
$ git pull
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), 696 bytes | 174.00 KiB/s, done.
From github.com:USERNAME/sample_project
  be62476..605b6a7 main    -> origin/main
Updating be62476..605b6a7
Fast-forward
 main.py | 1 +
 1 file changed, 1 insertion(+)

```

Again, the command's output provides all the details about the operation. Note that `git pull` will download the remote branch and update the local branch in a single step.
If we want to download the remote branch without updating the local one, then we can use the `[git fetch](https://git-scm.com/docs/git-fetch)` command. This practice gives us the chance to review the changes and commit them to our local repo only if they look right.
For example, go ahead and update the remote copy of `main.py` by adding another statement like `print("Let's go!!")`. Commit the changes. Then get back to your local repo and run the following command:
shell ```
$ git fetch
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), 731 bytes | 243.00 KiB/s, done.
From github.com:USERNAME/sample_project
  605b6a7..ba489df main    -> origin/main

```

This command downloaded the latest changes from `origin/main` to our local repo. Now we can compare the remote copy of `main.py` to the local copy. To do this, we can use the [`git diff`](https://git-scm.com/docs/git-diff) command as follows:
shell ```
$ git diff main origin/main
diff --git a/main.py b/main.py
index be2aa66..4f0e7cf 100644
--- a/main.py
+++ b/main.py
@@ -1,3 +1,4 @@
 print('Hello, World!')
 print('Welcome to PythonGUIs!')
 print("Your Git Tutorial is Here...")
+print("Let's go!!")

```

In the command's output, you can see that the remote branch adds a line containing `print("Let's go!!")` to the end of `main.py`. This change looks good, so we can use `git pull` to commit the change automatically.
### Exploring Alternatives to GitHub
While GitHub is the most popular public Git server and collaboration platform in use, it is far from being the only one. [GitLab.com](https://about.gitlab.com) and [BitBucket](https://bitbucket.org) are popular commercial alternatives similar to GitHub. While they have paid plans, both offer free plans, with some restrictions, for individual users.
Although, if you would like to use a completely open-source platform instead, [Codeberg](https://codeberg.org) might be a good option. It's a community-driven alternative with a focus on supporting [Free Software](https://en.wikipedia.org/wiki/Free_software). Therefore, in order to use Codeberg, your project needs to use a [compatible open-source license](https://docs.codeberg.org/getting-started/faq/#is-it-allowed-to-host-non-free-software%3F).
Optionally, you can also run your own Git server. While you could just use barebones `git` for this, software such as [GitLab Community Edition (CE)](https://gitlab.com/rluna-gitlab/gitlab-ce) and [Forgejo](https://forgejo.org/) provide you with both the benefits of running your own server and the experience of using a service like GitHub.
## Conclusion
By now, you're able to use Git for version-controlling your projects. Git is a powerful tool that will make you much more efficient and productive, especially as the scale of your project grows over time.
While this guide introduced you to most of its basic concepts and common commands, Git has many more commands and options that you can use to be even more productive. Now, you know enough to get up to speed with Git.
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Lalin Paranawithana](https://www.pythonguis.com/static/theme/images/authors/lalin-paranawithana.jpg)](https://www.pythonguis.com/authors/lalin-paranawithana/)
**Getting Started With Git and GitHub in Your Python Projects** was written by [Lalin Paranawithana](https://www.pythonguis.com/authors/lalin-paranawithana/) with contributions from [Leo Well](https://www.pythonguis.com/authors/leo-well/) . 
Lalin is a technology enthusiast with a focus on Linux and digital privacy. Lalin is currently trying to learn Python so he can build paid, open source applications and libraries with Linux as a first-class citizen. 
**Getting Started With Git and GitHub in Your Python Projects** was published in [tutorials](https://www.pythonguis.com/tutorials/) on March 20, 2023 (updated April 08, 2025) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[git](https://www.pythonguis.com/topics/git/) [github](https://www.pythonguis.com/topics/github/) [python](https://www.pythonguis.com/topics/python/) [version-control](https://www.pythonguis.com/topics/version-control/) [ getting-started](https://www.pythonguis.com/topics/getting-started/)
  * [](https://www.pythonguis.com/ "Python GUIs")
  * [Databases & SQL](https://www.pythonguis.com/topics/databases/)
  * [Learn the fundamentals](https://www.pythonguis.com/topics/foundation/)
  * [Where do I begin?](https://www.pythonguis.com/topics/getting-started/)
  * [Data Science](https://www.pythonguis.com/topics/data-science/)
  * [Packaging & Distribution](https://www.pythonguis.com/topics/packaging/)
  * [QML/QtQuick](https://www.pythonguis.com/topics/qml/)
  * [Raspberry Pi](https://www.pythonguis.com/topics/raspberry-pi/)
  * [Games](https://www.pythonguis.com/topics/games/)
  * [Intermediate Tutorials](https://www.pythonguis.com/topics/intermediate/)


  * **Sections**
  * [Installation](https://www.pythonguis.com/installation/)
  * [First steps with PySide6](https://www.pythonguis.com/tutorials/pyside6-creating-your-first-window/)
  * [First steps with PyQt6](https://www.pythonguis.com/tutorials/pyqt6-creating-your-first-window/)
  * [Example Python Apps](https://www.pythonguis.com/examples/)
  * [Widget Library](https://www.pythonguis.com/widgets/)
  * [Simple PyQt6 & PySide6 documentation](https://www.pythonguis.com/docs/)
  * [Reusable code & snippets](https://www.pythonguis.com/code/)
  * [Frequently Asked Questions](https://www.pythonguis.com/faq/)


  * **Tutorials**
  * [Which Python GUI library?](https://www.pythonguis.com/faq/which-python-gui-library/)
  * [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/)
  * [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/)
  * [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/)
  * [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/)
  * [Tkinter tutorial](https://www.pythonguis.com/tkinter-tutorial/)
  * [Latest articles](https://www.pythonguis.com/blog/)


  * **Books & Downloads**
  * [ Your Downloads](https://www.martinfitzpatrick.com/library/)
  * [PyQt5 Book](https://www.pythonguis.com/pyqt5-book/) / [PySide2 Book](https://www.pythonguis.com/pyside2-book/)
  * [PyQt6 Book](https://www.pythonguis.com/pyqt6-book/) / [PySide6 Book](https://www.pythonguis.com/pyside6-book/)
  * [Python Packaging Book](https://www.pythonguis.com/packaging-book/)
  * [ Book Source Code](https://www.pythonguis.com/books/downloads/)
  * [ PyQt6 Video Course](https://www.martinfitzpatrick.com/pyqt6-crash-course/)


  * **Community & Consulting**
  * [ Python GUIS Forum ](https://forum.pythonguis.com/)
  * [ Feedback & Corrections](https://tally.so/r/wbvxNE)
  * [Consulting](https://www.pythonguis.com/hire/)
  * [Mentoring](https://www.pythonguis.com/live/)
  * [Contact me](https://www.martinfitzpatrick.com/contact)
  * [Licensing, Privacy & Legal](https://www.martinfitzpatrick.com/legal)


[](https://twitter.com/pythonguis) [](https://github.com/pythonguis) [](https://www.facebook.com/pythonguis) [](https://www.youtube.com/channel/UCMW4KwSlygaDef0tgqPjbRQ) [](https://www.linkedin.com/company/pythonguis/)
[Python GUIs](https://www.pythonguis.com/) Copyright ©2014-2025 [ Martin Fitzpatrick](https://www.martinfitzpatrick.com)
Tutorials CC-BY-NC-SA [Sitemap](https://www.pythonguis.com/sitemap/) [Changelog](https://www.pythonguis.com/changelog/) Public code [BSD](https://opensource.org/licenses/BSD-2-Clause) & [MIT](https://opensource.org/licenses/MIT)
