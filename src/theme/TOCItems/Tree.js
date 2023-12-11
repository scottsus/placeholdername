import React from 'react';
import Link from '@docusaurus/Link';

function TOCItemTree({ toc, className, linkClassName, isChild }) {
  if (!toc.length) {
    return null;
  }
  return (
    <ul className={isChild ? undefined : className}>
      {toc.map((heading) => (
        <li key={heading.id}>
          <Link
            to={`#${heading.id}`}
            className={linkClassName ?? undefined}
            style={{ fontSize: '1.4em', marginBottom: '1em' }}
            // Developer provided the HTML, so assume it's safe.
            dangerouslySetInnerHTML={{ __html: heading.value }}
          />
          <TOCItemTree
            isChild
            toc={heading.children}
            className={className}
            linkClassName={linkClassName}
          />
        </li>
      ))}
    </ul>
  );
}
// Memo only the tree root is enough
export default React.memo(TOCItemTree);
