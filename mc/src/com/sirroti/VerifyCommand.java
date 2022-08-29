package com.sirroti;

import java.sql.ResultSet;
import java.sql.SQLException;

import net.md_5.bungee.api.CommandSender;
import net.md_5.bungee.api.chat.TextComponent;
import net.md_5.bungee.api.connection.ProxiedPlayer;
import net.md_5.bungee.api.plugin.Command;

public class VerifyCommand extends Command{
    public VerifyCommand() { super("verify"); }

    public void execute(CommandSender sender, String[] args) {
        if (args.length < 1) {
            sender.sendMessage(new TextComponent("§bVerifySystem §7» §cBitte gebe deinen Discord Namen+Tag (bsp. KLAPPI#3843) an!")); 
            return;
        }

        ProxiedPlayer author = (ProxiedPlayer) sender;
        MySql.send("CREATE TABLE IF NOT EXISTS Users(uuid varchar(40), mc_name varchar(16), dc_name varchar(100), role varchar(30), code int, status int)");

        ResultSet author_info = MySql.get("SELECT * FROM Users WHERE uuid='"+author.getUniqueId().toString()+"'");
        Boolean empty = false;
        try {
            empty = author_info.next();
        } catch (SQLException e1) { e1.printStackTrace(); }

        try {
            if (empty != false) {
                if (author_info.getInt(6) == 0) {
                    sender.sendMessage(new TextComponent("§bVerifySystem §7» §cDu warst bereits im Verify Vorgang!\n§bVerifySystem §7» §cWenn etwas nicht geklappt hat kannst du deine Daten mit /verify_reset resetten")); 
                    return;
                }
            }
        } catch (SQLException e) { e.printStackTrace(); }

        try {
            if (empty == false) {
                MySql.send("INSERT INTO Users (uuid, mc_name, dc_name, role, status) VALUES ('"+author.getUniqueId().toString()+"', '"+author.getName()+"', '"+args[0]+"', '"+Utils.get_rank(author)+"', 1)"); 
                author.sendMessage(new TextComponent("§bVerifySystem §7» §aDir wurde erfolgreich eine Verify-Nachricht gesendet.\n§bVerifySystem §7» §2Dies kann bis zu 10 Sekunden dauern!"));
                return;
            }
            if (author_info.getInt(6) == 2) {
                if (author_info.getInt(5) == Integer.parseInt(args[0])) {
                    MySql.send("UPDATE Users SET status=3 WHERE uuid='"+author.getUniqueId().toString()+"'");
                    author.sendMessage(new TextComponent("§bVerifySystem §7» §aDu wurdest erfolgreich verifiziert!"));
                } else {
                    author.sendMessage(new TextComponent("§bVerifySystem §7» §cDies ist der Falsche Code\n§bVerifySystem §7» §cWenn etwas nicht geklappt hat kannst du deine Daten mit /verify_reset resetten"));
                }
        }} catch (SQLException e) { e.printStackTrace(); }
    }
}