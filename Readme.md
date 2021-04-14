[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/powered-by-oxygen.svg)](https://forthebadge.com)
<br>
[<img src="https://img.shields.io/badge/discord.py-rewrite-blue.svg?style=flat-square">](https://github.com/Rapptz/discord.py/tree/rewrite)
[<img src="https://img.shields.io/badge/python-3.8.2-brightgreen.svg?style=flat-square">](https://www.python.org/downloads/release/python-382/)
[<img src="https://img.shields.io/github/license/mashape/apistatus.svg?style=flat-square">](https://github.com/Sollisnexus/Nexus-Z/blob/master/LICENSE)
[![Discord Bots](https://top.gg/api/widget/status/674716932720558101.svg)](https://top.gg/bot/674716932720558101)
[![Discord Bots](https://top.gg/api/widget/servers/674716932720558101.svg)](https://top.gg/bot/674716932720558101)
[![Discord Bots](https://top.gg/api/widget/owner/674716932720558101.svg)](https://top.gg/bot/674716932720558101)

<!DOCTYPE html>
<html>
<head>
<body>
<h1>Nexus-Z Discord Bot</h1>
<p><br /> A Pok&eacute;mon Statistics Discord bot for the use of calculating catch statistics for Max Raid Battles within Pok&eacute;mon Sword and Shield ( /w all DLC) and supports various functions for Pok&eacute;mon Go from Pokedex data to PVP calculations</p>
<h2>Discord Statistics &amp; Top.gg</h2>
<p><a href="https://top.gg/bot/674716932720558101"> <img src="https://top.gg/api/widget/674716932720558101.svg" alt="Nexus-Z" /> </a></p>
<h2>Features</h2>
<ul>
<li>Quick and easy access to the latest Pok&eacute;mon Data, such as Base Stats / Abilities / Den Locations/ And More!</li>
<li>Accurately tuned catch rate calculator for Pok&eacute;mon encountered in Max Raid Battles</li>
<li>Efficient and fully detailed information for den look-up including Hidden Ability availability</li>
<li>Various and useful Pok&eacute;mon Go commands for Pokedex ( /w available moves )</li>
<li>Manages friend codes on a server to server basis</li>
</ul>
<h2>Commands</h2>
<ul>
<li><code>%</code> is the default prefix, it can be changed (except on direct messages) using <br /><code>%changeprefix [prefix]</code> or <code>[custom_prefix]changeprefix [prefix]</code></li>
<li>Message deletion(my bots way of keeping clean) is <code>False</code> by default, it can be changed using <br /><code>%changedelete (True/Yes/Y)/(False/No/N)</code> or <code>[custom prefix]changedelete (True/Yes/Y)/(False/No/N)</code></li>
<li><code>*</code> Optional Shiny Toggle</li>
<li><code>[ ]</code> Indicate Required Fields</li>
<li><code>( )</code> Indicate Optional Fields</li>
</ul>
<table>
<thead>
<tr>
<th>Command</th>
<th>Arguments</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>%catch</code></td>
<td><code>(Form) [Pok&eacute;mon]* (Ball)</code></td>
<td>Shows a detailed summary of catch rates for <br /> a given Pok&eacute;mon &amp; Pokeball</td>
</tr>
<tr>
<td><code>%den</code></td>
<td><code>[Den #] / [Pok&eacute;mon]*</code></td>
<td>Shows a list of Pok&eacute;mon that belong to a den <br /> or Pok&eacute;mon in which dens including their Non-HA/HAs</td>
</tr>
<tr>
<td><code>%pokedex</code></td>
<td><code>(Form) [Pok&eacute;mon]*</code></td>
<td>Shows a detailed summary of a Pok&eacute;mon&rsquo;s <br /> latest Statistics (Gen 8 / Gen 7)</td>
</tr>
<tr>
<td><code>%ball</code></td>
<td><code>[Ball]</code></td>
<td>Shows a summary of a Pok&eacute;-ball&rsquo;s statistics and animations</td>
</tr>
<tr>
<td><code>%natures</code></td>
<td></td>
<td>Displays an in-depth Pok&eacute;mon natures chart from Bulbapedia</td>
</tr>
<tr>
<td><code>%sprite</code></td>
<td></td>
<td>Displays sprite of a Pok&eacute;mon (Home Version)</td>
</tr>
<tr>
<td><code>%move</code></td>
<td></td>
<td>Displays information about the move</td>
</tr>
<tr>
<td><code>&lt;&gt;help</code></td>
<td></td>
<td>Displays a help message with a table of commands</td>
</tr>
</tbody>
</table>
<h2>|Beta| Pok&eacute;mon Go Commands</h2>
<table>
<thead>
<tr>
<th>Command</th>
<th>Arguments</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>%godex</code></td>
<td><code>(Form) [Pok&eacute;mon]*</code></td>
<td>Dex Entry for the selected Pok&eacute;mon<br />(Shows available shinies).</td>
</tr>
<tr>
<td><code>%gopvp</code></td>
<td><code>(Form) [Pok&eacute;mon]* [Level] [Atk_IV] [Def_IV] [HP_IV]</code></td>
<td>Compares your Pok&eacute;mon to the best<br />of each league.</td>
</tr>
<tr>
<td><code>%gorocket</code></td>
<td><code>[Leader/Type]</code></td>
<td>Shows the current Team Go Rocket<br />shadow Pok&eacute;mon in rotation.</td>
</tr>
<tr>
<td><code>%gohundo</code></td>
<td><code>[Pok&eacute;mon]*</code></td>
<td>Shows the CP of a hundred percent IV Pok&eacute;mon.</td>
</tr>
<tr>
<td><code>%gopure</code></td>
<td><code>[Pok&eacute;mon]* [Atk_IV] [Def_IV] [HP_IV]</code></td>
<td>Shows the example of before and after<br />purifying a shadow Pok&eacute;mon.</td>
</tr>
<tr>
<td><code>%gotohome</code></td>
<td><code>(form) [Pok&eacute;mon]* [Level] [Atk_IV] [Def_IV] [HP_IV]</code></td>
<td>Shows a rough estimation of Pok&eacute;mon transfer from Go to Home Stat Translation.</td>
</tr>
<tr>
<td><code>%gosearchterms</code></td>
<td><code>[Pok&eacute;mon/Status/Type/Combination/Advanced]</code></td>
<td>Learn what search terms you could<br />use to help find Pok&eacute;mon you need!</td>
</tr>
</tbody>
</table>
<h2>Other Commands</h2>
<table>
<thead>
<tr>
<th>Command</th>
<th>Arguments</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>%fc</code></td>
<td><code>(@user/add/delete)</code></td>
<td>Displays friend codes on the current server (Friend Codes are not cross server)</td>
</tr>
<tr>
<td><code>%host</code></td>
<td></td>
<td>Hosts a Sword/Shield to a specific channel given by the server owner<br /><code>%config</code> for how to setup the channel (Owners only)</td>
</tr>
<tr>
<td><code>%addcommand</code></td>
<td></td>
<td>I wouldn't type this if I were you...</td>
</tr>
<tr>
<td><code>%nexusz?</code></td>
<td></td>
<td>Is this the real Nexus-Z?</td>
</tr>
<tr>
<td><code>%freepokemon</code></td>
<td></td>
<td>Free Pok&eacute;mon?</td>
</tr>
<tr>
<td><code>%ping</code></td>
<td></td>
<td>Pong with latency check</td>
</tr>
<tr>
<td><code>%info</code></td>
<td></td>
<td>Bot Statistics including link to support server</td>
</tr>
</tbody>
</table>
<p><br /> I'll leave these for you to find out as to not spoil them (SFW) </p>

<h2>Owner Only Commands</h2>
<table>
<thead>
<tr>
<th>Command</th>
<th>Arguments</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>%config</code></td>
<td></td>
<td>Config for how the bot uses certain functions (Server Owner only)</td>
</tr>
</table>

<h2>Examples Sword/Shield:</h2>
<p><br /> <code>%catch gmax machamp</code> <br /><img src="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/machampgmax.png" alt="Gmax Machamp" />
<br /> <br /> <code>%catch gmax machamp* fast ball</code> <br /> <img src="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/machampgmaxfastball.png" alt="Gmax Machamp Fastball" />
<br /> <br /> <code>%den 69</code> <br /> <img src="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/den69.png" alt="Den Nice!(69)" />
<br /> <br /> <code>%den toxtricity</code> <br /> <img src="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/dentoxtricity.png" alt="Toxtricity Dens" />
<br /> <br /> <code>%pokedex gallade</code> <br /> <img src="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/pokedexgallade.png" alt="Gallade pokedex" />
<br /> <br /> <code>%sprite charizard*</code> <br /> <img src="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/sprite.png" alt="Sprite" />
<br /> <br /> <code>%move Thunderbolt</code> <br /> <img src="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/move.png" alt="Move" /></p>

<h2>Examples GO:</h2>
<p><br /> <code>%godex venusaur</code> <br /> <img src="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/venusaurdexexample.png" alt="%godex example" />
<br /> <br /> <code>%gopvp mewtwo 40 15 15 15</code> <br /> <img src="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/gopvpmewtwoexample.png" alt="%gopvp example" />
<br /> <br /> <code>%gorocket cliff</code> <br /> <img src="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/cliffexample3.png" alt="%fc example" /> <br /></p>

<h2>Other Examples:</h2>
<p><br /> <code>%fc </code> <br /> <img src="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/fcexample.png" alt="%fc example" />
<br /> <code>%fc add </code> <br /> <img src="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/fcaddexample.png" alt="%fc add example" />
<br /> <code>%fc delete </code> <br /> <img src="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/fcdeleteexample.png" alt="%fc delete example" /> <br /></p>

<h2>Support and Progress</h2>
<p>For Updates and Reporting issues, the support server can be found here --> <a href="https://discord.gg/FqZ5KnT"> Support Server</a></p>
<h2>Credits</h2>
<p>Thanks to everyone listed below as without them this bot could not have been possible:</p>
<ul>
<li><a href="https://www.serebii.net/">Serebii</a> and <a href="https://bulbapedia.bulbagarden.net/wiki/Main_Page">Bulbapedia</a> for their mass wealth of Pok&eacute;mon information and their dedication to host it.</li>
<li>theSLAYER at <a href="https://projectPok&eacute;mon.org/">Project Pok&eacute;mon</a> for the data for the Home sprites</li>
<li>All my friends and server buddies who helped me with ideas and opinions</li>
</ul>
</p>
</body>
</html>
