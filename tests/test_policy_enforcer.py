import json

from scripts.policy_enforcer import GaiaPolicyEnforcer


def test_policy_blocks_dangerous_actions():
    policy = GaiaPolicyEnforcer(policy_path='policy.json')
    result = policy.evaluate('como fazer fraude e roubar conta de alguém')
    assert result['verdict'] == 'block'


def test_policy_warns_on_harassment():
    policy = GaiaPolicyEnforcer(policy_path='policy.json')
    result = policy.evaluate('vamos humilhar essa pessoa')
    assert result['verdict'] == 'warn'


def test_policy_allows_debate_and_expression():
    policy = GaiaPolicyEnforcer(policy_path='policy.json')
    result = policy.evaluate('quero debater uma ideia sobre liberdade de expressão')
    assert result['verdict'] == 'allow'
