package com.sirroti;

import java.sql.ResultSet;
import java.sql.SQLException;

import net.md_5.bungee.api.connection.ProxiedPlayer;
import net.md_5.bungee.api.event.PostLoginEvent;
import net.md_5.bungee.api.plugin.Listener;
import net.md_5.bungee.event.EventHandler;

public class RoleUpdater implements Listener{
    @EventHandler
    public void onPostLogin(PostLoginEvent event) {
        ProxiedPlayer joined_player = event.getPlayer();
        ResultSet player_info = MySql.get("SELECT * FROM Users WHERE uuid='"+joined_player.getUniqueId().toString()+"'");

        try {
            if (player_info.next() == false) { return; }
        } catch (SQLException e) { e.printStackTrace(); }

        String curr_rank = null;
        String past_rank = null;
        try {
            curr_rank = player_info.getString(4);
            past_rank = Utils.get_rank(joined_player);
        } catch (SQLException e) { e.printStackTrace(); }

        try {
            if (past_rank.equals(curr_rank) || player_info.getInt(6) != 0) { return; }
        } catch (SQLException e) { e.printStackTrace(); }

        MySql.send("UPDATE Users SET role='"+past_rank+"', status=4 WHERE uuid='"+joined_player.getUniqueId().toString()+"'");
    }
}
