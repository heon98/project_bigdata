from django.shortcuts import render
from django.http import HttpResponse
import torch
import transformers
import random
from torch import tensor
from transformers import AutoModelWithLMHead, PreTrainedTokenizerFast

import re

# Create your views here.

def hello_world(request):
    if request.method == "GET":
        category_text = str(request.GET.get('category'))
        taste_text = str(request.GET.get('taste'))
        quantity_text = str(request.GET.get('quantity'))
        delivery_text = str(request.GET.get('delivery'))
        menu_text = str(request.GET.get('menu_text'))

        tokenizer = PreTrainedTokenizerFast.from_pretrained('tokenizer_backup')
        if category_text != 'None':
            model = AutoModelWithLMHead.from_pretrained(category_text+'_model')

            if menu_text == 'None':
                prom = '맛' + taste_text + ' / ' + '양' + quantity_text + ' / ' + '배달' + delivery_text + ' / '
            else:

                prom = '맛' + taste_text + ' / ' + '양' + quantity_text + ' / ' + '배달' + delivery_text + ' / ' + menu_text

            sentence = ''
            prompt_ids = tokenizer.encode(prom)
            inp = tensor(prompt_ids)[None]
            preds = model.generate(inp,
                                    min_length = 50,
                                    max_length=300,
                                    pad_token_id=tokenizer.pad_token_id,
                                    eos_token_id=tokenizer.eos_token_id,
                                    bos_token_id=tokenizer.bos_token_id,
                                    repetition_penalty=2.0,
                                    use_cache=True,
                                    do_sample=True
                                    )
            sentence = tokenizer.decode(preds[0].cpu().numpy())
            print(sentence)
            sentence = sentence[16:-4].replace('<unk>','')


        else:
            sentence = '카테고리는 필수로 선택해 주세요!'



        return render(request, 'review_text_app/hello_world.html',
                      context={'trained_text': sentence})
