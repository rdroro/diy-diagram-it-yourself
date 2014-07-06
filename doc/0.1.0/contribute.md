Contribute
==========

@todo : Improve this page. 

Just few indications for contributors (and for me if I'll forget)

## Code

All python code must be pep8lized. To check if your code is correct just install pep8 and run :

        $ cd bin/ && pep8 *.py | grep -v E501

Use `grep -v` to escape _line too long_ warning

Check these following folders :

* `bin/`
* `bin/exceptions`
* `tests/unit-test`

### Characters encoding

* All python files must contains encoding description. At the first line add :

        # -*- coding: utf8 -*-

* Input and output string must be stored as <unicode> type. If some function accept only <str> type parameters just convert them and decode them after

### Unit Test

Write unit test for your class. Test :

* Return value
* Exceptions raised
* Parameters
* And of course the logic of your code

## Git

Before commit :

* run pep8 on each folders
* run unit tests : `$ cd tests && ./run-test.sh`

Try to respect these advices for commit messages [http://robots.thoughtbot.com/5-useful-tips-for-a-better-commit-message](http://robots.thoughtbot.com/5-useful-tips-for-a-better-commit-message)



