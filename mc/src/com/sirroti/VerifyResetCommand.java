package com.sirroti;

import java.sql.ResultSet;
import java.sql.SQLException;

import net.md_5.bungee.api.CommandSender;
import net.md_5.bungee.api.chat.TextComponent;
import net.md_5.bungee.api.connection.ProxiedPlayer;
import net.md_5.bungee.api.plugin.Command;

public class VerifyResetCommand extends Command{
    public VerifyResetCommand() { super("verify_reset"); }

    public void execute(CommandSender sender, String[] args) {
        ProxiedPlayer author = (ProxiedPlayer) sender;

        // MySql.connect();
        ResultSet author_info = MySql.get("SELECT * FROM Users WHERE uuid='"+author.getUniqueId().toString()+"'");

        try {
            if (author_info.next() == false) {
               author.sendMessage(new TextComponent("§bVerifySystem §7» §cDu hast keine Verify Daten!"));
               return;
            }
        } catch (SQLException e) { e.printStackTrace(); }

        MySql.send("DELETE FROM Users WHERE uuid='"+author.getUniqueId().toString()+"'");
        author.sendMessage(new TextComponent("§bVerifySystem §7» §aVerify Daten gelöscht"));
    }
}