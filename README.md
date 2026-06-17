# Table of Contents
- [Table of Contents](#table-of-contents)
- [Introduction](#introduction)
- [How it works](#how-it-works)
- [Want notifications?](#want-notifications)
- [Useful Resources](#useful-resources)

# Introduction  
Over the last few years, there has been a large influx of Japanese players into the MLB. Being half Japanese-American, much of my family feels represented by and takes pride in these players — especially due to my family's involvement in collegiate and professional sports. I built this tracker for them. Who has the time to sit down and watch a full baseball games these days?

# How it works
First, I created a list of players that I wanted to track. I include their name, their team, and their MLB Stats player ID. Then, using the MLB Stats API, I am able to find each player and, using my AtBatDetector object, detect when tracked players come on deck or are up to bat. When the object detects a change to a tracked player, it then sends a message to Discord via webhook. Then everyone who has enabled message notifications receives an update that the player is up to bat.

# Want notifications?
Join the Discord server here: https://discord.gg/yeYPG3tZKB

# Useful Resources
* https://github.com/toddrob99/MLB-StatsAPI/wiki/Endpoints
  * Wiki of MLB Stats API endpoints
* https://gdx.mlb.com/components/copyright.txt
  * Copyright information
