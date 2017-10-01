<div align=center>

<h2>Alpha version of jupyternotebook analyzator</h2>
<p><b>Work in progress..</b></p>

<p>
	<h3><b>NEPOUZIVAT</b></h3>
	<ul>
		<li>
			get_proc_usr()
		</li>
		<li>
			if_left_on()
		</li>
	</ul>
</p>
</div>

<div align=left>
<p>
	<h3><b>POUZITIE FUNKCI</b></h3>
	<ol>
		<li>
			get_data()=nacitava data, vracia zoznam riadkov
		</li>
		<br>
		<li>
			login(date,data)= date=hladany datum v en formate, data ziskame predoslou funkciu,vracia zoznam prihlasenych
		</li>
		<br>
		<li>
			logout(date,data)= tak ako predtym, vracia zoznam odhlasenych
		</li>
		<br>
		<li>
			neuplne(date,data)= vracia rozdiel medzi login logut, nemusi to znamenat nevyhnutne ze sa neodhlasil, celkom buggy
		</li>
		<br>
		<li>
			last_seven_days(data,name)= vrati kolkokrat bol dany user prihlaseny za poslednych 7 dni - neoverene
		</li>
		<br>
		<li>
			last_x_days(data,name,x)= tak ako predosla, akurat x = poctu dni ktore chceme dozadu, <b>nad 15 zacina buggovat!!!</b>
		</li>
	</ol
</div>
