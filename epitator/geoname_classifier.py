"""
This script was generated by the train.py script in this repository:
https://github.com/ecohealthalliance/geoname-annotator-training
"""
import numpy as np
from numpy import array, int32


HIGH_CONFIDENCE_THRESHOLD = 0.5
GEONAME_SCORE_THRESHOLD = 0.13
base_classifier =\
{
    'penalty': 'l1',
    'dual': False,
    'tol': 0.0001,
    'C': 0.1,
    'fit_intercept': True,
    'intercept_scaling': 1,
    'class_weight': None,
    'random_state': None,
    'solver': 'liblinear',
    'max_iter': 100,
    'multi_class': 'warn',
    'verbose': 0,
    'warm_start': False,
    'n_jobs': None,
    'classes_': array([False,  True]),
    'coef_': array([[
        # log_population
        0.3429166761571069,
        # name_count
        0.21709830611570793,
        # names_used
        0.8269376580293233,
        # exact_name_match
        0.7878854182406542,
        # multiple_spans
        0.42317571947152266,
        # span_length
        0.11635624170666362,
        # all_acronyms
        -2.328731808328372,
        # cannonical_name_used
        2.385204467844477,
        # loc_NE_portion
        0.9329501759634057,
        # other_NE_portion
        -0.2987093084510809,
        # noun_portion
        0.0,
        # num_tokens
        0.6928142361575395,
        # med_token_prob
        -0.3397337893668447,
        # exact_alternatives
        -0.9036023140885108,
        # PPL_feature_code
        -0.9397288188035898,
        # ADM_feature_code
        -1.2550824212955247,
        # PCL_feature_code
        2.5134423822820797,
        # other_feature_code
        0.0,
        # first_order
        1.1084960371415022,
        # combined_span
        1.4932312460013852,
        # close_locations
        0.0,
        # very_close_locations
        0.0,
        # base_score
        0.0,
        # base_score_margin
        0.0,
        # contained_locations
        0.0,
        # containing_locations
        0.0,
    ]]),
    'intercept_': array([-13.1126576]),
    'n_iter_': array([39], dtype=int32),
}

contextual_classifier =\
{
    'penalty': 'l1',
    'dual': False,
    'tol': 0.0001,
    'C': 0.1,
    'fit_intercept': True,
    'intercept_scaling': 1,
    'class_weight': None,
    'random_state': None,
    'solver': 'liblinear',
    'max_iter': 100,
    'multi_class': 'warn',
    'verbose': 0,
    'warm_start': False,
    'n_jobs': None,
    'classes_': array([False,  True]),
    'coef_': array([[
        # log_population
        0.31206770841202336,
        # name_count
        0.2005454877333416,
        # names_used
        0.648225709888574,
        # exact_name_match
        0.26445683289728583,
        # multiple_spans
        0.3307522320457672,
        # span_length
        0.12130650943509746,
        # all_acronyms
        -2.163337787453372,
        # cannonical_name_used
        2.3090619705615563,
        # loc_NE_portion
        1.4508913007712096,
        # other_NE_portion
        0.0,
        # noun_portion
        0.0,
        # num_tokens
        0.7907962702562655,
        # med_token_prob
        -0.2923973470351299,
        # exact_alternatives
        -0.8011614417553122,
        # PPL_feature_code
        -0.5475447417562185,
        # ADM_feature_code
        -0.9261497922203902,
        # PCL_feature_code
        2.299107106153456,
        # other_feature_code
        0.0,
        # first_order
        1.033140751957464,
        # combined_span
        0.36278895602219524,
        # close_locations
        0.12774614812147872,
        # very_close_locations
        -0.01864384833938384,
        # base_score
        -1.478626994083764,
        # base_score_margin
        2.5041655302244554,
        # contained_locations
        0.1104326082786128,
        # containing_locations
        0.40453329344238753,
    ]]),
    'intercept_': array([-12.44492995]),
    'n_iter_': array([36], dtype=int32),
}

# Logistic regression code from scipy
def predict_proba(X, classifier):
    """Probability estimation for OvR logistic regression.
    Positive class probabilities are computed as
    1. / (1. + np.exp(-classifier.decision_function(X)));
    multiclass is handled by normalizing that over all classes.
    """
    prob = np.dot(X, classifier['coef_'].T) + classifier['intercept_']
    prob = prob.ravel() if prob.shape[1] == 1 else prob
    prob *= -1
    np.exp(prob, prob)
    prob += 1
    np.reciprocal(prob, prob)
    if prob.ndim == 1:
        return np.vstack([1 - prob, prob]).T
    else:
        # OvR normalization, like LibLinear's predict_probability
        prob /= prob.sum(axis=1).reshape((prob.shape[0], -1))
        return prob


def predict_proba_base(X):
    return predict_proba(X, base_classifier)


def predict_proba_contextual(X):
    return predict_proba(X, contextual_classifier)
