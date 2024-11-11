## Put your title here

#### semver tag:
- #major: incompatible API, datamodel or business logic changes
- #minor: add or remove functionality in a backward compatible manner
- #patch: backward compatible bug fixes

Give a brief summary of the feature or bugfix using the semantic versioning structure below.
[Optionally] Describe the impact in has.

[UI/UX] Include a media file

[Optionally] Jira ticket link: https://repowerednl.atlassian.net/browse/REP-

[merge] <- triggers deploy

### Example Feature (to be removed)

## Add model FunnyAnimals without Alembic migration

#### #minor: Add model FunnyAnimals

For testing the alembic migration workflow, a model was added without creating a migration.

Now, when running the workflow, the migration test fails (as wanted) resulting in a GitHub Job Summary report, explaining that the migration for FunnyAnimals has not been created.

[merge]