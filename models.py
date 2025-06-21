from dataclasses import dataclass
from typing import Optional


@dataclass
class FatecContasReceber:
    idcr: Optional[int] = None
    documento: Optional[str] = None
    titulo: Optional[int] = None
    parcela: Optional[int] = None
    id_cliente: Optional[int] = None
    razao_cliente: Optional[str] = None
    nome_fantasia: Optional[str] = None
    id_grupo_cliente: Optional[int] = None
    descricao_grupo_cliente: Optional[str] = None
    cidade: Optional[str] = None
    uf: Optional[str] = None
    valor_titulo: Optional[str] = None
    valor_recebido: Optional[str] = None
    valor_saldo: Optional[str] = None
    data_emissao: Optional[str] = None
    data_entrada: Optional[str] = None
    data_vencimento: Optional[str] = None


@dataclass
class FatecClientes:
    id_cliente: Optional[int] = None
    razao_cliente: Optional[str] = None
    nome_fantasia: Optional[str] = None
    cidade: Optional[str] = None
    uf: Optional[str] = None
    id_grupo: Optional[int] = None
    descricao_grupo: Optional[str] = None


@dataclass
class FatecProdutos:
    codigo: Optional[str] = None
    descricao_produto: Optional[str] = None
    id_grupo: Optional[str] = None
    descricao_grupo: Optional[str] = None


@dataclass
class FatecVendas:
    id_venda: Optional[int] = None
    data_emissao: Optional[str] = None
    tipo: Optional[int] = None
    descricao_tipo: Optional[str] = None
    id_cliente: Optional[int] = None
    razao_cliente: Optional[str] = None
    nome_fantasia: Optional[str] = None
    id_grupo_cliente: Optional[int] = None
    descricao_grupo_cliente: Optional[str] = None
    cidade: Optional[str] = None
    uf: Optional[str] = None
    codigo_produto: Optional[str] = None
    descricao_produto: Optional[str] = None
    id_grupo_produto: Optional[int] = None
    descricao_grupo_produto: Optional[str] = None
    qtde: Optional[str] = None
    valor_unitario: Optional[str] = None
    total: Optional[str] = None
