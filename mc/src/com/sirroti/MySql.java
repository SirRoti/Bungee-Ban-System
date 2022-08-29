package com.sirroti;

import java.sql.Connection;
import java.sql.DriverManager;

import java.sql.ResultSet;

public class MySql {
    static String ip = "";
    static String port = "";
    static String database = "";
    static String username = "";
    static String pass = "";
    public static Connection con;
    
    public static Connection connect(){
        try {
        if (!isConnected()) {
            con = DriverManager.getConnection("jdbc:mysql://" + ip + ":" + port + "/" + database,username,pass);
            return con;
        } } catch (Exception error) { error.printStackTrace(); }
        return con;
    }
    
    public static void disconnect() {
        try {
            if(isConnected()) {
            con.close();
        } } catch (Exception error) { error.printStackTrace(); }
    }
    
    public static boolean isConnected() {
        if(con == null) { return false; }
        else { return true; }
    }
    
    public static ResultSet send(String qry) {
        try {
            con.prepareStatement(qry).executeUpdate();
        } catch (Exception error) { error.printStackTrace(); }
        return null;
    }

    public static ResultSet get(String qry) {
        try {
            ResultSet res = con.createStatement().executeQuery(qry);
            return res;
        } catch (Exception error) { error.printStackTrace(); }
        return null;
    }
}
