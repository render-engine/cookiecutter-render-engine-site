# Congratulations on setting up {{cookiecutter.SITE_TITLE}}!

This is your site to figure out what you want to do with it. This file exists to give you a 
little bit of direction in your next steps.

## Check the configuration

We've set up a default `pyproject.toml` for you with the default configuration for
- site
- module
- collection (if you chose to include a blog and/or a collection)

but this might not be the right configuration for you so you might want to double-check. Especially
if you went into `app.py` and changed any names around.

## GitHuB Workflows
We gave you a pair of example GitHub workflows:
- ExampleGitHubAction.yml - this example workflow is what you should use if you are managing the \
requirements with `requirements.txt` and using `pip`. Just copy the file over to `.github/workflows` \
and it will run automagically any time you push a change up.
- ExampleGitHubActionUV.yml - this example workflow is what you should use if you are managing the \
requirements with `uv`. Just copy the file over to `.github/workflows` and it will run automagically \
any time you push a change up.

## Seeing what you have
Run `render-engine serve` and a local copy of your site will be available to see at 
`http://localhost:8000`. Don't worry about remembering that or copying it from here - the console
will give you the link. If you add `--reload` to the command, it will rerender the site any time
there is a change to the `content` directory or one of the files in it. If you use the `--clean`
option it will remove any previous output directory before it renders the site.

## Adding content
Go a head and use the CLI to add a new page to one of your collections
```shell
render-engine new-entry <filename> [options]
```
This will create the content file and open the editor for you. Once you're done, check out what it 
looks like with `render-engine serve`.

## Need more help?
Check out the [documentation](https://render-engine.readthedocs.io/en/latest/) for more details on
what `render-engine` is capable of doing and how to use it.
