"""empty message

Revision ID: c4140403182b
Revises: d3edd01f9546
Create Date: 2020-06-10 21:29:53.328614

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c4140403182b'
down_revision = 'd3edd01f9546'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('empresa',
    sa.Column('id_empresa', sa.Integer(), nullable=False),
    sa.Column('nome_empresa', sa.Text(), nullable=False),
    sa.Column('cnpj', sa.Text(), nullable=False),
    sa.Column('email', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id_empresa')
    )
    op.create_table('produtosApk',
    sa.Column('id_produto', sa.Integer(), nullable=False),
    sa.Column('id_empresa', sa.Integer(), nullable=True),
    sa.Column('nome_produto', sa.Text(), nullable=False),
    sa.Column('descricao', sa.Text(), nullable=False),
    sa.Column('imagem', sa.Text(), nullable=False),
    sa.Column('preco', sa.Text(), nullable=False),
    sa.Column('quantidade', sa.Text(), nullable=False),
    sa.Column('promocao', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['id_empresa'], ['empresa.id_empresa'], ),
    sa.PrimaryKeyConstraint('id_produto')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('produtosApk')
    op.drop_table('empresa')
    # ### end Alembic commands ###
