package com.sirroti;

import java.sql.ResultSet;
import java.sql.SQLException;

import net.md_5.bungee.BungeeCord;
import net.md_5.bungee.api.chat.TextComponent;
import net.md_5.bungee.api.connection.ProxiedPlayer;
import net.md_5.bungee.api.event.PluginMessageEvent;
import net.md_5.bungee.api.plugin.Listener;

public class VerifyErrorDetect implements Listener{
    public static void onPluginMessage(PluginMessageEvent event) {
        ResultSet users = MySql.get("SELECT * FROM Users");
        try {
            while (users.next()) {
                if (users.getInt(6) != 5) { continue; }
                ProxiedPlayer player = BungeeCord.getInstance().getPlayer(users.getString(1));
                if (player != null) { player.sendMessage(new TextComponent("§bVerifySystem §7» §cDir konnte keine Verifizier Nachricht zugestellt werden. Bitte probiere es noch einmal.")); }
                MySql.send("DELETE FROM Users WHERE uuid='"+users.getString(1)+"'");
            }
        } catch (SQLException e) { e.printStackTrace(); }
    }
}