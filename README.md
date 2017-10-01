<div align=center>

<h2>Alpha version of jupyternotebook analyzator</h2>
<p><b>Work in progress..</b></p>
</div>
<div align=left>
<p>
	<h3><b>NEPOUZIVAT</b></h3>
	<ul>
		<li>
			<b>get_proc_usr()</b>
		</li>
		<li>
			<b>if_left_on()</b>
		</li>
	</ul>
</p>



<p>
	<h3><b>POUZITIE FUNKCI</b></h3>
	<ol>
		<li>
			<b>get_data()</b>=nacitava data, vracia zoznam riadkov
		</li>
		<br>
		<li>
			<b>login(date,data)</b>= date=hladany datum v en formate, data ziskame predoslou funkciu,vracia zoznam prihlasenych
		</li>
		<br>
		<li>
			<b>logout(date,data)</b> = tak ako predtym, vracia zoznam odhlasenych
		</li>
		<br>
		<li>
			<b>neuplne(date,data)</b> = vracia rozdiel medzi login logut, nemusi to znamenat nevyhnutne ze sa neodhlasil, celkom buggy
		</li>
		<br>
		<li>
			<b>last_seven_days(data,name)</b> = vrati kolkokrat bol dany user prihlaseny za poslednych 7 dni - neoverene
		</li>
		<br>
		<li>
			<b>last_x_days(data,name,x)</b> = tak ako predosla, akurat x = poctu dni ktore chceme dozadu, <b>nad 15 zacina buggovat!!!</b>
		</li>
	</ol
</div>
