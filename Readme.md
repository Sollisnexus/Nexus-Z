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
 <link rel="stylesheet" href="styles.css">
<body>
<h1>Nexus-Z Discord Bot</h1>
<br>
A Pokemon Statistics Discord bot for the use of calculating catch statistics for Max Raid Battles within Pokemon Sword and Shield (including Isle of Armor and The Crown Tundra)
<br>

<h2>Discord Statistics & Top.gg</h2>

<a href="https://top.gg/bot/674716932720558101" >
  <img src="https://top.gg/api/widget/674716932720558101.svg" alt="Nexus-Z" />
</a>

<h2>Features</h2>
<ul>
	<li>Quick and easy access to the latest Pokemon Data, such as Base Stats / Abilities / Den Locations/ And More!
	<li>Accurately tuned catch rate calculator for Pokemon encountered in Max Raid Battles
	<li>Effiecent and fully detailed information for den look-up including Hidden Ability availability
</ul>
<br>
<h2>Commands</h2>
	<li><code class="language-plaintext highlighter-rouge">%</code> is the default prefix, it can be changed using <code class="language-plaintext highlighter-rouge">%changeprefix [prefix]</code>or<code class="language-plaintext highlighter-rouge">[custom prefix]changeprefix [prefix]</code></li>
    <li><code class="language-plaintext highlighter-rouge">[ ]</code> Indicate Required Fields</li>
	<li><code class="language-plaintext highlighter-rouge">( )</code> Indicate Optional Fields</li>

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
		<td><code class="language-plaintext highlighter-rouge">%catch</code></td>
		<td><code class="language-plaintext highlighter-rouge">(Form) [Pokemon] (Ball)</code></td>
		<td>Shows a detailed summary of catch rates for a given Pokémon & Ball</td>
	</tr>
	<tr>
		<td><code class="language-plaintext highlighter-rouge">%den</code></td>
		<td><code class="language-plaintext highlighter-rouge">[Den #] / [Pokemon]</code></td>
		<td>Shows a list of Pokémon that belong to a den or Pokemon in which dens including their Non-HA/HAs</td>
	</tr>
<tr>
		<td><code class="language-plaintext highlighter-rouge">%pokedex</code></td>
		<td><code class="language-plaintext highlighter-rouge">(Form) [Pokemon]</code></td>
		<td>Shows a detailed summary of a Pokémon’s latest Statistics (Gen 8 / Gen 7)</td>
	</tr>
<tr>
		<td><code class="language-plaintext highlighter-rouge">%ball</code></td>
		<td><code class="language-plaintext highlighter-rouge">[Ball]</code></td>
		<td>Shows a summary of a Poké-ball’s statistics and animations </td>
	</tr>
<tr>
		<td><code class="language-plaintext highlighter-rouge">%natures</code></td>
		<td><code class="language-plaintext highlighter-rouge"></code></td>
		<td>Displays an in-depth Pokémon natures chart from Bulbapedia</td>
	</tr>
<tr>
		<td><code class="language-plaintext highlighter-rouge"><>help</code></td>
		<td><code class="language-plaintext highlighter-rouge"></code></td>
		<td>Displays a help message with a table of commands</td>
	</tr>
</tbody>
</table>
</p>
<p>
<br>
<h2> |Beta| Pokemon Go Commands</h2>
<br>
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
		<td><code class="language-plaintext highlighter-rouge">%godex</code></td>
		<td><code class="language-plaintext highlighter-rouge">(Form) [Pokemon]</code></td>
		<td>Dex Entry for the selected pokemon (Shows available shinies).</td>
	</tr>
	<tr>
		<td><code class="language-plaintext highlighter-rouge">%gopvp</code></td>
		<td><code class="language-plaintext highlighter-rouge">(Form) [Pokemon] [Level] [Atk_IV] [Def_IV] [HP_IV]</code></td>
		<td>Compares your pokemon to the best of each league.</td>
	</tr>
	<tr>
		<td><code class="language-plaintext highlighter-rouge">%gorocket</code></td>
		<td><code class="language-plaintext highlighter-rouge">[Leader/Type]</code></td>
		<td>Shows the current Team Go Rocket shadow Pokemon in rotation.</td>
	</tr>
  <tr>
		<td><code class="language-plaintext highlighter-rouge">%gohundo</code></td>
		<td><code class="language-plaintext highlighter-rouge">[Pokemon]</code></td>
		<td>Shows the CP of a hundred percent IV Pokemon.</td>
	</tr>
  <tr>
		<td><code class="language-plaintext highlighter-rouge">%gopure</code></td>
		<td><code class="language-plaintext highlighter-rouge">[Pokemon] [Atk_IV] [Def_IV] [HP_IV]</code></td>
		<td>Shows the example before and after of purifying a shadow Pokemon.</td>
	</tr>
  <tr>
		<td><code class="language-plaintext highlighter-rouge">%gotohome</code></td>
		<td><code class="language-plaintext highlighter-rouge">[Pokemon] [Level] [Atk_IV] [Def_IV] [HP_IV]</code></td>
		<td>Shows a rough estimation of Pokemon transfer from Go to Home Stat Translation.</td>
	</tr>
</tbody>
</table>
</p>
<p>
<br>
<h2>Other Commands</h2>
<br>
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
		<td><code class="language-plaintext highlighter-rouge">%addcommand</code></td>
		<td><code class="language-plaintext highlighter-rouge"></code></td>
		<td>I wouldn't type this if I were you...</td>
	</tr>
	<tr>
		<td><code class="language-plaintext highlighter-rouge">%nexusz?</code></td>
		<td><code class="language-plaintext highlighter-rouge"></code></td>
		<td>Is this the real Nexus-Z?</td>
	</tr>
  	<tr>
		<td><code class="language-plaintext highlighter-rouge">%freepokemon</code></td>
		<td><code class="language-plaintext highlighter-rouge"></code></td>
		<td>Free Pokemon?</td>
	</tr>
	<tr>
		<td><code class="language-plaintext highlighter-rouge">%ping</code></td>
		<td><code class="language-plaintext highlighter-rouge"></code></td>
		<td>Pong with latency check</td>
	</tr>
 	 <tr>
		<td><code class="language-plaintext highlighter-rouge">%info</code></td>
		<td><code class="language-plaintext highlighter-rouge"></code></td>
		<td>Bot Statistics including link to support server</td>
	</tr>
</tbody>
</table>
<br>
I'll leave these for you to find out as to not spoil them (SFW)
<br>
<br>
<h2>Examples Sw/Sh:</h2>
<br>
<code class="language-plaintext highlighter-rouge">%catch gmax machamp</code>
<br>
<img src="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/machampgmax.png" alt="Gmax Machamp">
<br>
<br>
<code class="language-plaintext highlighter-rouge">%catch gmax machamp fastball</code>
<br>
<img src="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/machampgmaxfastball.png" alt="Gmax Machamp Fastball">
<br>
<br>
<code class="language-plaintext highlighter-rouge">%den 69</code>
<br>
<img src="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/den69.png" alt="Den Nice!(69)">
<br>
<br>
<code class="language-plaintext highlighter-rouge">%den toxtricity</code>
<br>
<img src="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/dentoxtricity.png" alt="Toxtricity Dens">
<br>
<br>
<code class="language-plaintext highlighter-rouge">%pokedex gallade</code>
<br>
<img src="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/pokedexgallade.png" alt="Gallade pokedex">
<br>
<br>
<br>
<h2>Examples GO:</h2>
<br>
<code class="language-plaintext highlighter-rouge">%godex venusaur</code>
<br>
<img src="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/venusaurdexexample.png" alt="%godex example">
<br>
<br>
<code class="language-plaintext highlighter-rouge">%gopvp mewtwo 40 15 15 15</code>
<br>
<img src="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/gopvpmewtwoexample.png" alt="%gopvp example">
<br>
<br>
<code class="language-plaintext highlighter-rouge">%gorocket cliff</code>
<br>
<img src="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/cliffexample3.png" alt="%gorocket example">
<br>
<br>
	
<h2>Support and Progress</h2>
W.I.P
<br>
<h2>Credits</h2>
Thanks to everyone listed below as without them this bot could not have been possible:
<ul>
	<li><a href="https://www.serebii.net/">Serebii</a> and <a href="https://bulbapedia.bulbagarden.net/wiki/Main_Page">Bulbapedia</a> for their mass wealth of Pokémon information and their dedication to host it.
	<li>theSLAYER at <a href="https://projectpokemon.org/">Project Pokemon</a> for the data for the Home sprites
	<li>All my friends and server buddies who helped me with ideas and opinions
<ul>
</p>
</body>
</html>
