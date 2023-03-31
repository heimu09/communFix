from rest_framework import generics
from .models import Request
from .serializers import RequestSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response

import openai

from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Request
from .serializers import RequestSerializer

def get_gpt_response(prompt):
    openai.api_key = "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"
    response = openai.Completion.create(model="gpt-3.5-turbo-0301", prompt=prompt, temperature=0, max_tokens=500)
    print(response)
    result = response
    return result['choices'][0]['text']

def get_gpt_response(prompt, model="gpt-3.5-turbo", max_tokens=500, n=1, temperature=0.5):
    openai.api_key = "sk-5Ix0pz0DfUQWeyR4hzFzT3BlbkFJy2lTe8VEppRWQdwxa5"
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": prompt}],
        max_tokens=max_tokens,
        n=n,
        temperature=temperature,
    )

    return response.choices[0].message["content"]


class RequestList(generics.ListCreateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        description = request.data.get('description', None)

        if not description:
            return Response({"error": "Description is required."}, status=status.HTTP_400_BAD_REQUEST)
        gpt_response = get_gpt_response(f'Оцени ущерб заявки по 10 ти бальной шкале ответь только цифрой и все: {description} только одной цифрой')
        comment = get_gpt_response(f'Дай совет что делать кому обратиться я живу в квартире: {description}')
        print(comment)

        if gpt_response:
            request.data['complexity'] = gpt_response
            request.data['gpt_comment'] = comment

            return self.create(request, *args, **kwargs)

        else:
            return Response({"error": "GPT API request failed."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class RequestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    permission_classes = [IsAuthenticated]
