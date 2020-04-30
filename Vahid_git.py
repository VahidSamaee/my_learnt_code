'''
working with git

@ modified
#in order to initiate the git in a
a folder you have to:
#in CMD
#in the directory which you want to make 
a respitory 
>> git init

***************************
@ staging
# this command shows which
files are in the stage condition 
which can be commited
>> git status 


# in order to stage a file, you have
to use the following code
>> git add name_of_file


# in order to stage all the
files 
>> git add.


# in order to remove a file 
from the staging area:
>> git rm --cached name_of_file

**********************
@commiting

# in orther ot commit a file 
>> git commit -m "the logical comment 
				  for this commit point"



*******************
@ git log 
# in order to see the list of 
commited points
>> git log


# in order to see the list of
commited points in short
>> git log --oneline



***************************
@@ undoing things
@ check out commit  (very safe)
@ revert commit
@ reset commit  (unsafe, premanently delet the commits)



@check out
# in order to check out a commit in the past
>> git checkout id_of_commit_point

# in order to go back to normal condition
>> git checkout master 



@revert commit
# In order to undo a commit in commit list you 
can use this 
>>git revert id_of_commit_point 
 


@ tp reset to an specific commit, in this way you will delet all the nest commits
# if you want to keep the changes you have made then 
>> git reset id_of_commit_point 

# if you need to delete the changes and literally bring back 
to that commit point then 
>> git reset id_of_commit_point --hard



***************************
@ branching
#in orther to make a new branch
>> git branch name_of_branch
or
>> git checkout -b name_of_branch



# if you want to see all the branches
>> git branch -a

# to switch to a branch
>> git checkout branch_name

#after this all the modifuication, changes, adding, delling,
staging and commiting will be added to this branch


# in order to back to the master branch
>> git checkout master
(you will see all the new features are not present here)



# to delete a brach first go to the master branch and then 
>>git branch -D name_of_branch



******************************
@ merging branches and dealing with confilicts
# the first thing is you have to be in
the branch that you want to merge in

>> git merge name_of_branch


@ confilict
when confilict happens during the merging
eddit the file in the branch in which merging is happening.
delete all the extra features which GIT 
has added such as <<<<  >>>>>  ===== and make the final code in that part \
and then make a commit without any name

>> git add .
>> git commit 
in new blue list
>> :wq







*********************************
@@@ github introduction


# case one: you have already a respitory on
your PC

1- make a respitory online
2- copy the URL which gives
3- then:
>> git push the_URL the_name_of_branch


# If you make changes, then you can also
push the changes
1- apply the changes on your pc repo
2- make commitment 
3- puch whole of the repo to the github


# in order to avoind to find, copy and past
the github repo, you can define an alias, 
how:
>> git remote add alias(like original) the_URL 








# case two: first making a repo online
1- again you make a new repo on git hub
(you can add readme test file in this condition)
2- then you use the "Clone or download"
3- then you copy the provided URL
4- then cmd go to the location where you
want to make your repo
5- you Clone you repo in this location,
How:
>> git clone URL 


# for re pushing
-since the code is cloned, you can 
simply use dollowing code
>> git remote -v
and then you can us the alian present
in the information.
>> git push original master





*************************************
#collabrating on github

https://www.youtube.com/watch?v=MnUd31TvBoU

*************************************
#forking and distributing

https://www.youtube.com/watch?v=HbSjyU2vf6Y

*****************************


'''

