# cd "Python\Projects\For big project"
# git status -> Show what you changed


# Add and push
# git add .
# git commit -m "Note"
# git push
# -> Github update

# To pull the latest version: git pull


# 1. If we work on a new feature or bug fix -> create a new branch
# git checkout -b (name)
# -> git checkout -b feature-refactor ->name is feature-refractors
# 2. make changes
# git add .
# git commit -m "change what"
# git push origin feature-refactor #push to that branch
# 3. go to github and open Pull Request
# when you change something: add a pull request and put it there so your friend can review and comment or approve
# once approved, click Merge pull request to merge into #main branch
# 4. after merging:
# git checkout main
# git pull
# ->now your main branch is fully updated
