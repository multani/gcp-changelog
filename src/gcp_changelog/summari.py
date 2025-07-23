import os
from typing import Iterator
from typing import cast

from langchain.chat_models import init_chat_model

from .models import ChangelogEntry
from .models import Index
from .models import Summary


class Summarizer:
    def __init__(self) -> None:
        if "GOOGLE_API_KEY" not in os.environ:
            raise ValueError(
                "GOOGLE_API_KEY environment variable is not set. "
                "Please set it to use the Google Gemini model."
            )

        llm = init_chat_model(
            "gemini-2.5-flash-lite",
            model_provider="google_genai",
        )
        self.llm = llm.with_structured_output(Summary)

    def summarize_index(self, index: Index) -> Iterator[Summary | None]:
        for product, changelog in index.products.items():
            for date, entries in changelog.entries.items():
                for entry in entries:
                    if entry.summary is not None:
                        yield None
                        continue

                    summary = self.summarize_entry(entry)
                    entry.summary = summary

                    yield summary

    def summarize_entry(self, changelog: ChangelogEntry) -> Summary:
        prompt = f"""Can you make 2 summaries?
        1. One very short, for a title. No references to Google Cloud, don't overuse capitalized words
        2. A bit longer (2 or 3 sentences, maximum)

        The kind of the announcement is: {changelog.kind}

        The content to summarize is the following:
        {changelog.content}
        """

        response = self.llm.invoke(prompt)
        response = cast(Summary, response)
        return response
