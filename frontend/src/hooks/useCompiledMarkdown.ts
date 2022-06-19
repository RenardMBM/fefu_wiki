import {computed, ref} from "vue";
// @ts-ignore
import {marked} from 'marked';

export default function useCompiledMarkdown (markdownText: string) {
    const postMarkdown = ref(markdownText);
    const compiledMarkdown = computed(() => {
        return marked(postMarkdown.value, {sanitize: true});
    })
    return {
        postMarkdown: postMarkdown, compiledMarkdown
    }
}