### Bash environment

> [!NOTE]
> Do this **only once**, at your first connection, after [downloading the material](git_tp_course.md).

To set up your bash environment (useful aliases, prompt, loading of the modules…), copy two configuration files in a terminal:

```bash
cd $HOME
cp script-locmarca/Setup_training/p.bash_profile ~/.bash_profile
cp script-locmarca/Setup_training/p.bashrc ~/.bashrc
```

Then close the terminal and open a new one, so that the new configuration is loaded.

You can check the configuration with:

- aliases: type `alias`
- loaded modules: type `module list`
