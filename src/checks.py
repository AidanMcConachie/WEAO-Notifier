import config

load = []

if config.synapse==True:
    load.append("synapse")
if config.scriptware==True:
    load.append("scriptware")
if config.krnl==True:
    load.append("krnl")
if config.temple==True:
    load.append("temple")
if config.electron==True:
    load.append("electron")
if config.skisploit==True:
    load.append("skisploits")
if config.wearedevs==True:
    load.append("wearedevs")
if config.oxygenu==True:
    load.append("oxygenu")
if config.fluxus==True:
    load.append("fluxus")
if config.celery==True:
    load.append("celery")
if config.roware==True:
    load.append("roware")
if config.westeria==True:
    load.append("westeria")
if config.dx9ware==True:
    load.append("dx9ware")
if config.atlas==True:
    load.append("atlas")