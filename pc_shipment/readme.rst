==========================
Test 2: PC Shipment
==========================

A module for the test tw: PC Shipment.

the schema can be found in the folder /schema

to install this module in odoo, you will need odoo 15.
Here I use a docker compose, so if it possible you can run it with the docker-compose.yml i provided.
For that you will need Docker to be installed, then run the command: docker compose up in the same folder.

This module can be run independently, it only required the base module of odoo to run.
After install, you can find it int the menu with the name PC Shipment.

For this module, I managed to get the function to update the quantity on hand based on Product move.
But I still have not able to make it so that the product quantity will be update based on the location.
Due to that, the delivery request function is still not completed