package com.example.informster;

import android.os.StrictMode;
import android.util.Log;
import android.view.View;
import android.widget.TextView;

import androidx.annotation.LongDef;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class Connect {
    public static Connection getConnection(String Hospital_ID)
    {
       String ip =  "192.168.1.31";
       String port =  "1433";
       String uname = "SA";
       String database =  Hospital_ID;
       String pass =  "Enter your password here" 
       Connection conn =  null;

       String driver =  "net.sourceforge.jtds.jdbc.Driver";
       StrictMode.ThreadPolicy policy =  new StrictMode.ThreadPolicy.Builder().permitAll().build();
       StrictMode.setThreadPolicy(policy);
       try
       {
           Class.forName("net.sourceforge.jtds.jdbc.Driver");
           String ConnectionURL= "jdbc:jtds:sqlserver://"+ ip + ":"+ port+";"+ "databasename="+ database+";user="+uname+";password="+pass+";";
           Log.d("Shaury", "getConnection: " + ConnectionURL);
           conn =  DriverManager.getConnection(ConnectionURL);
           return conn;
       } catch (SQLException | ClassNotFoundException se ) {
           Log.d("Connection Failed",  "getConnection: " +  se.getMessage());
       }
    return  conn;
    }

}
