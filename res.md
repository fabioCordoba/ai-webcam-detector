{
'res':
{
'input_path': './placa.jpg',
'page_index': None,
'model_settings':
{
'use_doc_preprocessor': True,
'use_textline_orientation': True
},
'doc_preprocessor_res':
{
'input_path': None,
'page_index': None,
'model_settings':
{
'use_doc_orientation_classify': True,
'use_doc_unwarping': True
},
'angle': 0
},
'text_det_params':
{
'limit_side_len': 64,
'limit_type': 'min',
'thresh': 0.3,
'max_side_limit': 4000,
'box_thresh': 0.6,
'unclip_ratio': 1.5
},
'text_type': 'general',
'textline_orientation_angles': array([0]),
'text_rec_score_thresh': 0.0,
'return_word_box': False,
'rec_texts': ['0UO-14G'],
'rec_scores': array([0.80413711]),
'rec_polys': array([[[ 0, 14],
        ...,
        [ 0, 41]]], shape=(1, 4, 2), dtype=int16), 'rec_boxes': array([[0, ..., 41]], shape=(1, 4), dtype=int16)
}
}
