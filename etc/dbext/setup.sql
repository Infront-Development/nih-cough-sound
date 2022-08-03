IF NOT EXISTS(SELECT * from sys.databases where name = 'coughsounddb')
    BEGIN
        CREATE DATABASE coughsounddb;
    END 
GO  
USE coughsounddb;
GO          