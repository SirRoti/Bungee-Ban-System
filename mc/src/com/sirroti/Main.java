package com.sirroti;

import net.md_5.bungee.api.plugin.Plugin;

public class Main extends Plugin{
    @Override
    public void onEnable() {
        MySql.connect();
        getProxy().getPluginManager().registerListener(this, new RoleUpdater());
        getProxy().getPluginManager().registerCommand(this, new VerifyCommand());
        getProxy().getPluginManager().registerCommand(this, new VerifyResetCommand());
        getLogger().info("Plugin Loaded");
    }
}
