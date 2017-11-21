-- Script Date: 21/11/2017 3:33 AM  - ErikEJ.SqlCeScripting version 3.5.2.74
-- Database information:
-- Database: .\revoDB.db
-- ServerVersion: 3.18.0
-- DatabaseSize: 208 KB
-- Created: 20/11/2017 10:13 PM

-- User Table information:
-- Number of tables: 16
-- Ability: -1 row(s)
-- AbilityType: -1 row(s)
-- AoeAbility: -1 row(s)
-- AttackSpeedCooldown: -1 row(s)
-- AttackStyle: -1 row(s)
-- BindingAbility: -1 row(s)
-- BleedingAbility: -1 row(s)
-- BuffEffect: -1 row(s)
-- BuffTime: -1 row(s)
-- CritBoostAbility: -1 row(s)
-- DebilitatingAbility: -1 row(s)
-- PunishingAbility: -1 row(s)
-- Setting: -1 row(s)
-- SpecialAbility: -1 row(s)
-- SpecialBleedingAbility: -1 row(s)
-- WalkingAbility: -1 row(s)

SELECT 1;
PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE [Setting] (
  [Name] nvarchar(25)  NOT NULL
, [Value] nvarchar(25)  NOT NULL
, [Description] nvarchar(25)  NOT NULL
, CONSTRAINT [sqlite_autoindex_Setting_1] PRIMARY KEY ([Name])
);
CREATE TABLE [AttackStyle] (
  [Style] nvarchar(10)  NOT NULL
, CONSTRAINT [sqlite_autoindex_AttackStyle_1] PRIMARY KEY ([Style])
);
CREATE TABLE [AttackSpeedCooldown] (
  [Speed] nvarchar(10)  NOT NULL
, [value] float NOT NULL
, CONSTRAINT [sqlite_autoindex_AttackSpeedCooldown_1] PRIMARY KEY ([Speed])
);
CREATE TABLE [AbilityType] (
  [Type] nvarchar(1)  NOT NULL
, CONSTRAINT [sqlite_autoindex_AbilityType_1] PRIMARY KEY ([Type])
);
CREATE TABLE [Ability] (
  [Name] nvarchar(25)  NOT NULL
, [Type] nvarchar(1)  NOT NULL
, [Damage] float NOT NULL
, [Ready] bit NOT NULL
, [Style] nvarchar(10)  NOT NULL
, [Time] float NOT NULL
, [Cooldown] float NOT NULL
, CONSTRAINT [sqlite_autoindex_Ability_1] PRIMARY KEY ([Name])
, FOREIGN KEY ([Style]) REFERENCES [AttackStyle] ([Style]) ON DELETE NO ACTION ON UPDATE NO ACTION
, FOREIGN KEY ([Type]) REFERENCES [AbilityType] ([Type]) ON DELETE NO ACTION ON UPDATE NO ACTION
);
CREATE TABLE [AoeAbility] (
  [Name] nvarchar(25)  NOT NULL
, CONSTRAINT [sqlite_autoindex_AoeAbility_1] PRIMARY KEY ([Name])
, FOREIGN KEY ([Name]) REFERENCES [Ability] ([Name]) ON DELETE NO ACTION ON UPDATE NO ACTION
);
CREATE TABLE [BindingAbility] (
  [Name] nvarchar(25)  NOT NULL
, CONSTRAINT [sqlite_autoindex_BindingAbility_1] PRIMARY KEY ([Name])
, FOREIGN KEY ([Name]) REFERENCES [Ability] ([Name]) ON DELETE NO ACTION ON UPDATE NO ACTION
);
CREATE TABLE [BleedingAbility] (
  [Name] nvarchar(25)  NOT NULL
, [Value] float NOT NULL
, CONSTRAINT [sqlite_autoindex_BleedingAbility_1] PRIMARY KEY ([Name])
, FOREIGN KEY ([Name]) REFERENCES [Ability] ([Name]) ON DELETE NO ACTION ON UPDATE NO ACTION
);
CREATE TABLE [BuffEffect] (
  [Name] nvarchar(25)  NOT NULL
, [Value] float NOT NULL
, CONSTRAINT [sqlite_autoindex_BuffEffect_1] PRIMARY KEY ([Name])
, FOREIGN KEY ([Name]) REFERENCES [Ability] ([Name]) ON DELETE NO ACTION ON UPDATE NO ACTION
);
CREATE TABLE [BuffTime] (
  [Name] nvarchar(25)  NOT NULL
, [Value] float NOT NULL
, CONSTRAINT [sqlite_autoindex_BuffTime_1] PRIMARY KEY ([Name])
, FOREIGN KEY ([Name]) REFERENCES [Ability] ([Name]) ON DELETE NO ACTION ON UPDATE NO ACTION
);
CREATE TABLE [CritBoostAbility] (
  [Name] nvarchar(25)  NOT NULL
, CONSTRAINT [sqlite_autoindex_CritBoostAbility_1] PRIMARY KEY ([Name])
, FOREIGN KEY ([Name]) REFERENCES [Ability] ([Name]) ON DELETE NO ACTION ON UPDATE NO ACTION
);
CREATE TABLE [DebilitatingAbility] (
  [Name] nvarchar(25)  NOT NULL
, CONSTRAINT [sqlite_autoindex_DebilitatingAbility_1] PRIMARY KEY ([Name])
, FOREIGN KEY ([Name]) REFERENCES [Ability] ([Name]) ON DELETE NO ACTION ON UPDATE NO ACTION
);
CREATE TABLE [PunishingAbility] (
  [Name] nvarchar(25)  NOT NULL
, CONSTRAINT [sqlite_autoindex_PunishingAbility_1] PRIMARY KEY ([Name])
, FOREIGN KEY ([Name]) REFERENCES [Ability] ([Name]) ON DELETE NO ACTION ON UPDATE NO ACTION
);
CREATE TABLE [SpecialAbility] (
  [Name] nvarchar(25)  NOT NULL
, CONSTRAINT [sqlite_autoindex_SpecialAbility_1] PRIMARY KEY ([Name])
, FOREIGN KEY ([Name]) REFERENCES [Ability] ([Name]) ON DELETE NO ACTION ON UPDATE NO ACTION
);
CREATE TABLE [SpecialBleedingAbility] (
  [Name] nvarchar(25)  NOT NULL
, CONSTRAINT [sqlite_autoindex_SpecialBleedingAbility_1] PRIMARY KEY ([Name])
, FOREIGN KEY ([Name]) REFERENCES [Ability] ([Name]) ON DELETE NO ACTION ON UPDATE NO ACTION
);
CREATE TABLE [WalkingAbility] (
  [Name] nvarchar(25)  NOT NULL
, [Value] float NOT NULL
, CONSTRAINT [sqlite_autoindex_WalkingAbility_1] PRIMARY KEY ([Name])
, FOREIGN KEY ([Name]) REFERENCES [Ability] ([Name]) ON DELETE NO ACTION ON UPDATE NO ACTION
);
INSERT INTO [Setting] ([Name],[Value],[Description]) VALUES (
'AttackSpeed','2.4','Attack Speed');
INSERT INTO [Setting] ([Name],[Value],[Description]) VALUES (
'Bleeds','false','Bleeds');
INSERT INTO [Setting] ([Name],[Value],[Description]) VALUES (
'Gain','0','Gain');
INSERT INTO [Setting] ([Name],[Value],[Description]) VALUES (
'StartingAdrenaline','0','Starting Adrenaline');
INSERT INTO [Setting] ([Name],[Value],[Description]) VALUES (
'Stuns','true','Stuns');
INSERT INTO [Setting] ([Name],[Value],[Description]) VALUES (
'Time','300','Time');
INSERT INTO [Setting] ([Name],[Value],[Description]) VALUES (
'Unit','S','Seconds/Ticks');
INSERT INTO [AttackStyle] ([Style]) VALUES (
'Defensive');
INSERT INTO [AttackStyle] ([Style]) VALUES (
'Magic');
INSERT INTO [AttackStyle] ([Style]) VALUES (
'Melee');
INSERT INTO [AttackStyle] ([Style]) VALUES (
'Ranged');
INSERT INTO [AttackSpeedCooldown] ([Speed],[value]) VALUES (
'Average',3.6);
INSERT INTO [AttackSpeedCooldown] ([Speed],[value]) VALUES (
'Fast',3);
INSERT INTO [AttackSpeedCooldown] ([Speed],[value]) VALUES (
'Fastest',2.4);
INSERT INTO [AttackSpeedCooldown] ([Speed],[value]) VALUES (
'Slow',4.2);
INSERT INTO [AttackSpeedCooldown] ([Speed],[value]) VALUES (
'Slowest',7.2);
INSERT INTO [AbilityType] ([Type]) VALUES (
'B');
INSERT INTO [AbilityType] ([Type]) VALUES (
'T');
INSERT INTO [AbilityType] ([Type]) VALUES (
'U');
INSERT INTO [Ability] ([Name],[Type],[Damage],[Ready],[Style],[Time],[Cooldown]) VALUES (
'Asphyxiate','T',451.2,0,'Magic',5.4,20.4);
INSERT INTO [Ability] ([Name],[Type],[Damage],[Ready],[Style],[Time],[Cooldown]) VALUES (
'Assault','T',525.6,0,'Melee',5.4,30);
INSERT INTO [Ability] ([Name],[Type],[Damage],[Ready],[Style],[Time],[Cooldown]) VALUES (
'Backhand','B',60,1,'Melee',1.8,15);
INSERT INTO [Ability] ([Name],[Type],[Damage],[Ready],[Style],[Time],[Cooldown]) VALUES (
'Barge','B',75,1,'Melee',1.8,20.4);
INSERT INTO [Ability] ([Name],[Type],[Damage],[Ready],[Style],[Time],[Cooldown]) VALUES (
'Berserk','U',0,0,'Melee',1.8,60);
INSERT INTO [Ability] ([Name],[Type],[Damage],[Ready],[Style],[Time],[Cooldown]) VALUES (
'Binding Shot','B',60,1,'Ranged',1.8,15);
INSERT INTO [Ability] ([Name],[Type],[Damage],[Ready],[Style],[Time],[Cooldown]) VALUES (
'Blood Tendrils','T',324,0,'Melee',1.8,45);
INSERT INTO [Ability] ([Name],[Type],[Damage],[Ready],[Style],[Time],[Cooldown]) VALUES (
'Bombardment','T',131.4,0,'Ranged',1.8,30);
INSERT INTO [Ability] ([Name],[Type],[Damage],[Ready],[Style],[Time],[Cooldown]) VALUES (
'Chain','B',60,1,'Magic',1.8,10.2);
INSERT INTO [Ability] ([Name],[Type],[Damage],[Ready],[Style],[Time],[Cooldown]) VALUES (
'Cleave','B',112.8,1,'Melee',1.8,7.2);
INSERT INTO [Ability] ([Name],[Type],[Damage],[Ready],[Style],[Time],[Cooldown]) VALUES (
'Combust','B',241.2,1,'Magic',1.8,15);
INSERT INTO [Ability] ([Name],[Type],[Damage],[Ready],[Style],[Time],[Cooldown]) VALUES (
'Concentrated Blast','B',152.8,1,'Magic',3.6,5.4);
INSERT INTO [Ability] ([Name],[Type],[Damage],[Ready],[Style],[Time],[Cooldown]) VALUES (
'Corruption Blast','B',200,1,'Magic',1.8,15);
INSERT INTO [Ability] ([Name],[Type],[Damage],[Ready],[Style],[Time],[Cooldown]) VALUES (
'Corruption Shot','B',200,1,'Ranged',1.8,15);
INSERT INTO [Ability] ([Name],[Type],[Damage],[Ready],[Style],[Time],[Cooldown]) VALUES (
'Dazing Shot','B',94.2,1,'Ranged',1.8,5.4);
INSERT INTO [Ability] ([Name],[Type],[Damage],[Ready],[Style],[Time],[Cooldown]) VALUES (
'Deadshot','U',426.13,0,'Ranged',1.8,30);
INSERT INTO [Ability] ([Name],[Type],[Damage],[Ready],[Style],[Time],[Cooldown]) VALUES (
'Death''s Swiftness','U',0,0,'Ranged',1.8,60);
INSERT INTO [Ability] ([Name],[Type],[Damage],[Ready],[Style],[Time],[Cooldown]) VALUES (
'Debilitate','T',60,0,'Defensive',1.8,30);
INSERT INTO [Ability] ([Name],[Type],[Damage],[Ready],[Style],[Time],[Cooldown]) VALUES (
'Decimate','B',112.8,1,'Melee',1.8,7.2);
INSERT INTO [Ability] ([Name],[Type],[Damage],[Ready],[Style],[Time],[Cooldown]) VALUES (
'Deep Impact','T',120,0,'Magic',1.8,15);
INSERT INTO [Ability] ([Name],[Type],[Damage],[Ready],[Style],[Time],[Cooldown]) VALUES (
'Destroy','T',451.2,0,'Melee',4.2,20.4);
INSERT INTO [Ability] ([Name],[Type],[Damage],[Ready],[Style],[Time],[Cooldown]) VALUES (
'Detonate','T',225,0,'Magic',3.6,30);
INSERT INTO [Ability] ([Name],[Type],[Damage],[Ready],[Style],[Time],[Cooldown]) VALUES (
'Dismember','B',120.6,1,'Melee',1.8,15);
INSERT INTO [Ability] ([Name],[Type],[Damage],[Ready],[Style],[Time],[Cooldown]) VALUES (
'Dragon Breath','B',112.8,1,'Magic',1.8,10.2);
INSERT INTO [Ability] ([Name],[Type],[Damage],[Ready],[Style],[Time],[Cooldown]) VALUES (
'Flurry','T',204,0,'Melee',5.4,20.4);
INSERT INTO [Ability] ([Name],[Type],[Damage],[Ready],[Style],[Time],[Cooldown]) VALUES (
'Forceful Backhand','T',120,0,'Melee',1.8,15);
INSERT INTO [Ability] ([Name],[Type],[Damage],[Ready],[Style],[Time],[Cooldown]) VALUES (
'Fragmentation Shot','B',120.6,1,'Ranged',1.8,15);
INSERT INTO [Ability] ([Name],[Type],[Damage],[Ready],[Style],[Time],[Cooldown]) VALUES (
'Frenzy','U',610,1,'Melee',4.2,60);
INSERT INTO [Ability] ([Name],[Type],[Damage],[Ready],[Style],[Time],[Cooldown]) VALUES (
'Fury','B',152.8,1,'Melee',3.6,5.4);
INSERT INTO [Ability] ([Name],[Type],[Damage],[Ready],[Style],[Time],[Cooldown]) VALUES (
'Havoc','B',94.2,1,'Melee',1.8,10.2);
INSERT INTO [Ability] ([Name],[Type],[Damage],[Ready],[Style],[Time],[Cooldown]) VALUES (
'Hurricane','U',265,0,'Melee',1.8,20.4);
INSERT INTO [Ability] ([Name],[Type],[Damage],[Ready],[Style],[Time],[Cooldown]) VALUES (
'Impact','B',60,1,'Magic',1.8,15);
INSERT INTO [Ability] ([Name],[Type],[Damage],[Ready],[Style],[Time],[Cooldown]) VALUES (
'Kick','B',60,1,'Melee',1.8,15);
INSERT INTO [Ability] ([Name],[Type],[Damage],[Ready],[Style],[Time],[Cooldown]) VALUES (
'Massacre','U',426.13,0,'Melee',1.8,60);
INSERT INTO [Ability] ([Name],[Type],[Damage],[Ready],[Style],[Time],[Cooldown]) VALUES (
'Metamorphosis','U',0,0,'Magic',1.8,60);
INSERT INTO [Ability] ([Name],[Type],[Damage],[Ready],[Style],[Time],[Cooldown]) VALUES (
'Needle Strike','B',94.2,1,'Ranged',1.8,5.4);
INSERT INTO [Ability] ([Name],[Type],[Damage],[Ready],[Style],[Time],[Cooldown]) VALUES (
'Omnipower','U',300,0,'Magic',1.8,30);
INSERT INTO [Ability] ([Name],[Type],[Damage],[Ready],[Style],[Time],[Cooldown]) VALUES (
'Onslaught','U',532,0,'Defensive',4.8,120);
INSERT INTO [Ability] ([Name],[Type],[Damage],[Ready],[Style],[Time],[Cooldown]) VALUES (
'Overpower','U',300,0,'Melee',1.8,60);
INSERT INTO [Ability] ([Name],[Type],[Damage],[Ready],[Style],[Time],[Cooldown]) VALUES (
'Piercing Shot','B',56.4,1,'Ranged',1.8,3);
INSERT INTO [Ability] ([Name],[Type],[Damage],[Ready],[Style],[Time],[Cooldown]) VALUES (
'Pulverise','U',300,0,'Melee',1.8,60);
INSERT INTO [Ability] ([Name],[Type],[Damage],[Ready],[Style],[Time],[Cooldown]) VALUES (
'Punish','B',56.4,1,'Melee',1.8,3);
INSERT INTO [Ability] ([Name],[Type],[Damage],[Ready],[Style],[Time],[Cooldown]) VALUES (
'Quake','T',131.4,0,'Melee',1.8,20.4);
INSERT INTO [Ability] ([Name],[Type],[Damage],[Ready],[Style],[Time],[Cooldown]) VALUES (
'Rapid Fire','T',451.2,0,'Ranged',5.4,20.4);
INSERT INTO [Ability] ([Name],[Type],[Damage],[Ready],[Style],[Time],[Cooldown]) VALUES (
'Ricochet','B',60,1,'Ranged',1.8,10.2);
INSERT INTO [Ability] ([Name],[Type],[Damage],[Ready],[Style],[Time],[Cooldown]) VALUES (
'Sacrifice','B',60,1,'Defensive',1.8,30);
INSERT INTO [Ability] ([Name],[Type],[Damage],[Ready],[Style],[Time],[Cooldown]) VALUES (
'Sever','B',112.8,1,'Melee',1.8,15);
INSERT INTO [Ability] ([Name],[Type],[Damage],[Ready],[Style],[Time],[Cooldown]) VALUES (
'Shadow Tendrils','T',283,0,'Ranged',1.8,45);
INSERT INTO [Ability] ([Name],[Type],[Damage],[Ready],[Style],[Time],[Cooldown]) VALUES (
'Shatter','T',0,0,'Defensive',1.8,120);
INSERT INTO [Ability] ([Name],[Type],[Damage],[Ready],[Style],[Time],[Cooldown]) VALUES (
'Slaughter','T',145,0,'Melee',1.8,30);
INSERT INTO [Ability] ([Name],[Type],[Damage],[Ready],[Style],[Time],[Cooldown]) VALUES (
'Slice','B',75,1,'Melee',1.8,3);
INSERT INTO [Ability] ([Name],[Type],[Damage],[Ready],[Style],[Time],[Cooldown]) VALUES (
'Smash','B',94.2,1,'Melee',1.8,10.2);
INSERT INTO [Ability] ([Name],[Type],[Damage],[Ready],[Style],[Time],[Cooldown]) VALUES (
'Smoke Tendrils','T',345,0,'Magic',5.4,45);
INSERT INTO [Ability] ([Name],[Type],[Damage],[Ready],[Style],[Time],[Cooldown]) VALUES (
'Snap Shot','T',265,0,'Ranged',1.8,20.4);
INSERT INTO [Ability] ([Name],[Type],[Damage],[Ready],[Style],[Time],[Cooldown]) VALUES (
'Snipe','B',172,1,'Ranged',3.6,10.2);
INSERT INTO [Ability] ([Name],[Type],[Damage],[Ready],[Style],[Time],[Cooldown]) VALUES (
'Sonic Wave','B',94.2,1,'Magic',1.8,5.4);
INSERT INTO [Ability] ([Name],[Type],[Damage],[Ready],[Style],[Time],[Cooldown]) VALUES (
'Stomp','T',120,0,'Melee',1.8,15);
INSERT INTO [Ability] ([Name],[Type],[Damage],[Ready],[Style],[Time],[Cooldown]) VALUES (
'Storm Shards','B',0,1,'Defensive',1.8,30);
INSERT INTO [Ability] ([Name],[Type],[Damage],[Ready],[Style],[Time],[Cooldown]) VALUES (
'Sunshine','U',0,0,'Magic',1.8,60);
INSERT INTO [Ability] ([Name],[Type],[Damage],[Ready],[Style],[Time],[Cooldown]) VALUES (
'Tight Bindings','T',120,0,'Ranged',1.8,15);
INSERT INTO [Ability] ([Name],[Type],[Damage],[Ready],[Style],[Time],[Cooldown]) VALUES (
'Tsunami','U',250,0,'Magic',1.8,60);
INSERT INTO [Ability] ([Name],[Type],[Damage],[Ready],[Style],[Time],[Cooldown]) VALUES (
'Tuska''s Wrath','B',5940,1,'Defensive',1.8,120);
INSERT INTO [Ability] ([Name],[Type],[Damage],[Ready],[Style],[Time],[Cooldown]) VALUES (
'Unload','U',610,0,'Ranged',4.2,60);
INSERT INTO [Ability] ([Name],[Type],[Damage],[Ready],[Style],[Time],[Cooldown]) VALUES (
'Wild Magic','T',265,0,'Magic',4.8,20.4);
INSERT INTO [Ability] ([Name],[Type],[Damage],[Ready],[Style],[Time],[Cooldown]) VALUES (
'Wrack','B',56.4,1,'Magic',1.8,3);
INSERT INTO [AoeAbility] ([Name]) VALUES (
'Bombardment');
INSERT INTO [AoeAbility] ([Name]) VALUES (
'Chain');
INSERT INTO [AoeAbility] ([Name]) VALUES (
'Cleave');
INSERT INTO [AoeAbility] ([Name]) VALUES (
'Corruption Blast');
INSERT INTO [AoeAbility] ([Name]) VALUES (
'Corruption Shot');
INSERT INTO [AoeAbility] ([Name]) VALUES (
'Dragon Breath');
INSERT INTO [AoeAbility] ([Name]) VALUES (
'Flurry');
INSERT INTO [AoeAbility] ([Name]) VALUES (
'Hurricane');
INSERT INTO [AoeAbility] ([Name]) VALUES (
'Quake');
INSERT INTO [AoeAbility] ([Name]) VALUES (
'Ricochet');
INSERT INTO [AoeAbility] ([Name]) VALUES (
'Tsunami');
INSERT INTO [BindingAbility] ([Name]) VALUES (
'Barge');
INSERT INTO [BindingAbility] ([Name]) VALUES (
'Binding Shot');
INSERT INTO [BindingAbility] ([Name]) VALUES (
'Deep Impact');
INSERT INTO [BindingAbility] ([Name]) VALUES (
'Tight Bindings');
INSERT INTO [BleedingAbility] ([Name],[Value]) VALUES (
'Blood Tendrils',4.8);
INSERT INTO [BleedingAbility] ([Name],[Value]) VALUES (
'Combust',6);
INSERT INTO [BleedingAbility] ([Name],[Value]) VALUES (
'Corruption Blast',6);
INSERT INTO [BleedingAbility] ([Name],[Value]) VALUES (
'Corruption Shot',6);
INSERT INTO [BleedingAbility] ([Name],[Value]) VALUES (
'Deadshot',6);
INSERT INTO [BleedingAbility] ([Name],[Value]) VALUES (
'Dismember',6);
INSERT INTO [BleedingAbility] ([Name],[Value]) VALUES (
'Fragmentation Shot',6);
INSERT INTO [BleedingAbility] ([Name],[Value]) VALUES (
'Massacre',6);
INSERT INTO [BleedingAbility] ([Name],[Value]) VALUES (
'Shadow Tendrils',1.8);
INSERT INTO [BleedingAbility] ([Name],[Value]) VALUES (
'Slaughter',6);
INSERT INTO [BleedingAbility] ([Name],[Value]) VALUES (
'Smoke Tendrils',5.4);
INSERT INTO [BuffEffect] ([Name],[Value]) VALUES (
'Berserk',2);
INSERT INTO [BuffEffect] ([Name],[Value]) VALUES (
'Concentrated Blast',1.1);
INSERT INTO [BuffEffect] ([Name],[Value]) VALUES (
'Death''s Swiftness',1.5);
INSERT INTO [BuffEffect] ([Name],[Value]) VALUES (
'Fury',1.1);
INSERT INTO [BuffEffect] ([Name],[Value]) VALUES (
'Metamorphosis',1.625);
INSERT INTO [BuffEffect] ([Name],[Value]) VALUES (
'Needle Strike',1.07);
INSERT INTO [BuffEffect] ([Name],[Value]) VALUES (
'Piercing shot',2);
INSERT INTO [BuffEffect] ([Name],[Value]) VALUES (
'Punish',2);
INSERT INTO [BuffEffect] ([Name],[Value]) VALUES (
'Slice',1.506);
INSERT INTO [BuffEffect] ([Name],[Value]) VALUES (
'Sunshine',1.5);
INSERT INTO [BuffEffect] ([Name],[Value]) VALUES (
'Wrack',2);
INSERT INTO [BuffTime] ([Name],[Value]) VALUES (
'Barge',6.6);
INSERT INTO [BuffTime] ([Name],[Value]) VALUES (
'Berserk',19.8);
INSERT INTO [BuffTime] ([Name],[Value]) VALUES (
'Binding Shot',9.6);
INSERT INTO [BuffTime] ([Name],[Value]) VALUES (
'Concentrated Blast',5.4);
INSERT INTO [BuffTime] ([Name],[Value]) VALUES (
'Death''s Swiftness',30);
INSERT INTO [BuffTime] ([Name],[Value]) VALUES (
'Deep Impact',3.6);
INSERT INTO [BuffTime] ([Name],[Value]) VALUES (
'Forceful Backhand',3.6);
INSERT INTO [BuffTime] ([Name],[Value]) VALUES (
'Fury',5.4);
INSERT INTO [BuffTime] ([Name],[Value]) VALUES (
'Metamorphosis',15);
INSERT INTO [BuffTime] ([Name],[Value]) VALUES (
'Needle Strike',3.6);
INSERT INTO [BuffTime] ([Name],[Value]) VALUES (
'Rapid Fire',6);
INSERT INTO [BuffTime] ([Name],[Value]) VALUES (
'Stomp',3.6);
INSERT INTO [BuffTime] ([Name],[Value]) VALUES (
'Sunshine',30);
INSERT INTO [BuffTime] ([Name],[Value]) VALUES (
'Tight Bindings',9.6);
INSERT INTO [CritBoostAbility] ([Name]) VALUES (
'Berserk');
INSERT INTO [CritBoostAbility] ([Name]) VALUES (
'Concentrated Blast');
INSERT INTO [CritBoostAbility] ([Name]) VALUES (
'Death''s Swiftness');
INSERT INTO [CritBoostAbility] ([Name]) VALUES (
'Fury');
INSERT INTO [CritBoostAbility] ([Name]) VALUES (
'Metamorphosis');
INSERT INTO [CritBoostAbility] ([Name]) VALUES (
'Needle Strike');
INSERT INTO [CritBoostAbility] ([Name]) VALUES (
'Sunshine');
INSERT INTO [DebilitatingAbility] ([Name]) VALUES (
'Barge');
INSERT INTO [DebilitatingAbility] ([Name]) VALUES (
'Binding Shot');
INSERT INTO [DebilitatingAbility] ([Name]) VALUES (
'Deep Impact');
INSERT INTO [DebilitatingAbility] ([Name]) VALUES (
'Forceful Backhand');
INSERT INTO [DebilitatingAbility] ([Name]) VALUES (
'Rapid Fire');
INSERT INTO [DebilitatingAbility] ([Name]) VALUES (
'Stomp');
INSERT INTO [DebilitatingAbility] ([Name]) VALUES (
'Tight Bindings');
INSERT INTO [PunishingAbility] ([Name]) VALUES (
'Piercing Shot');
INSERT INTO [PunishingAbility] ([Name]) VALUES (
'Punish');
INSERT INTO [PunishingAbility] ([Name]) VALUES (
'Slice');
INSERT INTO [PunishingAbility] ([Name]) VALUES (
'Wrack');
INSERT INTO [SpecialAbility] ([Name]) VALUES (
'Detonate');
INSERT INTO [SpecialAbility] ([Name]) VALUES (
'Snipe');
INSERT INTO [SpecialBleedingAbility] ([Name]) VALUES (
'Deadshot');
INSERT INTO [SpecialBleedingAbility] ([Name]) VALUES (
'Massacre');
INSERT INTO [SpecialBleedingAbility] ([Name]) VALUES (
'Smoke Tendrils');
INSERT INTO [WalkingAbility] ([Name],[Value]) VALUES (
'Combust',1);
INSERT INTO [WalkingAbility] ([Name],[Value]) VALUES (
'Fragmentation Shot',1);
INSERT INTO [WalkingAbility] ([Name],[Value]) VALUES (
'Slaughter',1.5);
CREATE UNIQUE INDEX [UQ_Setting_Name] ON [Setting] ([Name] ASC);
CREATE UNIQUE INDEX [UQ_AttackStyle_Style] ON [AttackStyle] ([Style] ASC);
CREATE UNIQUE INDEX [UQ_AttackSpeedCooldown_value] ON [AttackSpeedCooldown] ([value] ASC);
CREATE UNIQUE INDEX [UQ_AttackSpeedCooldown_Speed] ON [AttackSpeedCooldown] ([Speed] ASC);
CREATE UNIQUE INDEX [UQ_AbilityType_Type] ON [AbilityType] ([Type] ASC);
CREATE UNIQUE INDEX [UQ_Ability_Name] ON [Ability] ([Name] ASC);
CREATE UNIQUE INDEX [UQ_AoeAbility_Name] ON [AoeAbility] ([Name] ASC);
CREATE UNIQUE INDEX [UQ_BindingAbility_Name] ON [BindingAbility] ([Name] ASC);
CREATE UNIQUE INDEX [UQ_BleedingAbility_Name] ON [BleedingAbility] ([Name] ASC);
CREATE UNIQUE INDEX [UQ_BuffEffect_Name] ON [BuffEffect] ([Name] ASC);
CREATE UNIQUE INDEX [UQ_BuffTime_Name] ON [BuffTime] ([Name] ASC);
CREATE UNIQUE INDEX [UQ_CritBoostAbility_Name] ON [CritBoostAbility] ([Name] ASC);
CREATE UNIQUE INDEX [UQ_DebilitatingAbility_Name] ON [DebilitatingAbility] ([Name] ASC);
CREATE UNIQUE INDEX [UQ_PunishingAbility_Name] ON [PunishingAbility] ([Name] ASC);
CREATE UNIQUE INDEX [UQ_SpecialAbility_Name] ON [SpecialAbility] ([Name] ASC);
CREATE UNIQUE INDEX [UQ_SpecialBleedingAbility_Name] ON [SpecialBleedingAbility] ([Name] ASC);
CREATE UNIQUE INDEX [UQ_WalkingAbility_Name] ON [WalkingAbility] ([Name] ASC);
COMMIT;

