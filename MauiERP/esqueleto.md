# ===MAUI ERP DICIONÁRIO ===
## OPERACIONAL [op]
- PRODUÇÕES [prod]
    - **INFORMAÇÕES** [ *inf* ] `Dados da produção`
        - **Descrição** [ *desc* `str`] `Nome completo da produção`
        - **Estampa** [ *est* ] `Código numérico da estampa e nome completo da estampa`
            - *Código* [ *cod* `int`]
            - *Nome* [ *nome* `str`]
        - **Ordem de Serviço** [ *op* `int`]
        - **Referência** [ *ref* `int`]
        - **Ordem de Produção** [ *op* `int`]
        - **Compra** [ *comp* ]
            - *Atacado* [ *atc* `str`]
            - *Varejo* [ *var* `str`]
            - *Rep. Atacado* [ *ratc* `str`]
            - *Rep. Varejo* [ *rvar* `str`]
            - *Atacado* [ *at* `str`]
        - **Programação** [ *prog* `str`]
        - **Data Alvo** [ *alvo* `int`]
        - **Recebimento** [ *receb* `str`]
            - **NFe** [ *nfe* `str`]
            - **Data** [ *data* `str`]
            - **Hora** [ *hora* `str`]
            - **Volumes** [ *vol* `int`]
                - *Caixas* [ *cx* `int`]
            - **Tecido** [ *tec* `float`]
            - **Aviamentos** [ *av* `str`]
            - **Obervações** [ *obs* `str`]
        - Produção
    - **CHAMADOS** [ *chmd* ]
        - **Código** [ *cod* `int`]
        - **Título** [ *titulo* `str`]
        - **Data** [ *data* ]
        - **Status** [ *stat* `str`]
- ENTREGAS [entrega]
    - NFe [nfe]
    - Data [data]
    - Hora [hora]
    - Tamanhos [tam]
    - Total [tamTotal]
    - Valor [valor]
    - Total Valor [valorTotal]
    
- FERRAMENTAS [ferram]
    - 90 dias [prazo90]
    - FICHAS [ficha]
        - Corte [corte]
        - Corte Mostruário [corteMost]
        - Controle Aviamentos [ctrlAv]
        - Checklist Aviamentos [checkAv]
- EFICIÊNCIA [efic]
    - DIÁRIA [dia]
	- MENSAL [mensal]
	- BONIFICAÇÃO [bonus]

Exemplos: opFerramPrazo90, opEficMensal, opProdEntregaNfe
##ADMINISTRATIVO [adm]
	<FUNCIONÁRIOS>
		<INFORMAÇÕES>
		<PRESENÇA>
			<SAÍDAS>
			<FALTAS>
			<ATESTADOS>
		<ASOS>
<COMPRAS>
	<DIÁRIO>
		<PADARIA>
			>PÃO
	<SEMANAL>
		<QUARTA FELIZ>
	<MENSAL>
		<PAPELARIA>
		<MERCADO>