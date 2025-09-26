---
title: postgresql
---

# Tipos

Abaixo descrevemos os tipos primitivos do PostgreSQL. 

(table-1)=
```
tipo                aliases         tamanho         descrição 
---------------------------------------------------------------------------------------------------------------------
SMALLINT            ---             2 bytes         inteiro com sinal de 16bits (1 bit para sinal, 15 bits para tamanho)
INTEGER             INT             4 bytes         inteiro com sinal de 32bits (1 bit para sinal, 31 bits para tamanho)
BIGINT              ---             8 bytes         inteiro com sinal de 64bits (1 bit para sinal, 63 bits para tamanho)
DECIMAL(N,M)        NUMERIC         variável        flutuante com <N> dígitos, sendo <M> depois do ponto
REAL                FLOAT4          4 bytes         flutuante com até 32bits
DOUBLE PRECISION    FLOAT8          8 bytes         flutuante com até 64bits
-------------------------------------------------------------------------------------------------------------------------
table 1: tipos numéricos em postgresql
```

(table-2)=
```
tipo                        aliases        tamanho         descrição
------------------------------------------------------------------------------------------------------------------------
CHARACTER(N)                CHAR           variável        strings com precisamente <N> caracteres
CHARACTER VARYING(N)        VARCHAR        variável        strings com até <N> caracteres      
TEXT                        ---            variável        strings de tamanho livre, limitadas a 1GB de armazenamento
------------------------------------------------------------------------------------------------------------------------
table 2: tipos de strings em postgresql
```

(table-3)=
```
tipo                             aliases         tamanho         descrição
--------------------------------------------------------------------------------------------------------------------------------------------
TIME WITHOUT TIME ZONE           TIME             8 bytes        tempo no formato 'hh:mm:ss.nnnnnn'
TIME WITH TIME ZONE              TIMETZ           12 bytes       tempo no formato 'hh:mm:ss.nnnnnn' junto de time zone 
TIMESTAMP WITHOUT TIME ZONE      TIMESTAMP        8 bytes        timestamp sem time zone no formato 'yyyy-mm-dd hh:mm:ss.nnnnnn'
TIMESTAMP WITH TIME ZONE         TIMESTAMPTZ      8 bytes        timestamp com time zone no formato 'yyyy-mm-dd hh:mm:ss.nnnnnn-tz'
---------------------------------------------------------------------------------------------------------------------------------------------
table 3: tipos de datetimes em postgresql
```

> Em PostgreSQL, dates, times and timestamps são recebidos como strings, mas armazenados como inteiros de tamanho fixo (número de dias desde 01-01-2000, número de micro segundos desde 00:00:00, e número de micro segundos desde 01-01-2000, respectivamente). 
